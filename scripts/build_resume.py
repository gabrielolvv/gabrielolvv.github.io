"""Generates dist/resume.pdf. Requires reportlab: pip install reportlab."""

from pathlib import Path

from reportlab.lib.colors import Color
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

OUTPUT = Path(__file__).resolve().parent.parent / "dist" / "resume.pdf"

INK = Color(0.066667, 0.094118, 0.078431)
ACCENT = Color(0.180392, 0.419608, 0.341176)
MUTED = Color(0.309804, 0.364706, 0.333333)
RULE = Color(0.905882, 0.92549, 0.913725)
MARGIN = 54.18898  # where text starts; the frame adds 6pt of padding on each side
FRAME_PADDING = 6
DATE_COLUMN = 84.4

name_style = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=24, leading=26, textColor=INK)
title_style = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=9.8, leading=11.5, textColor=ACCENT)
contact_style = ParagraphStyle("contact", fontName="Helvetica", fontSize=7.9, leading=9.6, textColor=MUTED)
summary_style = ParagraphStyle("summary", fontName="Helvetica", fontSize=9, leading=11.4, textColor=INK)
section_style = ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=8.8, leading=11, textColor=INK, spaceBefore=8, spaceAfter=3)
body_style = ParagraphStyle("body", fontName="Helvetica", fontSize=8.6, leading=10.7, textColor=INK)
entry_style = ParagraphStyle("entry", fontName="Helvetica-Bold", fontSize=9.1, leading=10.7, textColor=INK)
date_style = ParagraphStyle("date", fontName="Helvetica", fontSize=7.9, leading=9.5, textColor=MUTED, alignment=TA_RIGHT)
bullet_style = ParagraphStyle("bullet", parent=body_style, leftIndent=9, firstLineIndent=-7, spaceAfter=1.5)
link_style = ParagraphStyle("link", fontName="Helvetica", fontSize=8.1, leading=9.7, textColor=ACCENT, leftIndent=9)


def link(url, label):
    return f'<link href="{url}" color="#2e6b57">{label}</link>'


def entry(title, place, dates, bullets, url=None, label=None):
    heading = Table(
        [[Paragraph(f'{title} <font color="#2e6b57">- {place}</font>', entry_style), Paragraph(dates, date_style)]],
        colWidths=[A4[0] - 2 * MARGIN - DATE_COLUMN, DATE_COLUMN],
        hAlign="LEFT",
    )
    heading.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    flowables = [heading] + [Paragraph(f"- {text}", bullet_style) for text in bullets]
    if url:
        flowables.append(Paragraph(link(url, label), link_style))
    flowables.append(Spacer(1, 5))
    return flowables


def skill(label, text):
    return Paragraph(f"<b>{label}:</b> {text}", ParagraphStyle("skill", parent=body_style, spaceAfter=1.3))


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.5)
    canvas.line(34, 25, A4[0] - 34, 25)
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(MUTED)
    canvas.drawCentredString(A4[0] / 2, 14, "Gabriel Oliveira  -  Backend Engineering  -  Remote International Opportunities")
    canvas.restoreState()


def build():
    separator = '<font color="#4f5d55">&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;</font>'
    contact = separator.join([
        '<font color="#4f5d55">Fortaleza, Brazil</font>',
        link("mailto:gabrieloliv.dev@gmail.com", "gabrieloliv.dev@gmail.com"),
        link("https://www.linkedin.com/in/gabrielolvv/", "linkedin.com/in/gabrielolvv"),
        link("https://github.com/gabrielolvv", "github.com/gabrielolvv"),
        link("https://gabrielolvv.github.io/", "gabrielolvv.github.io"),
    ])

    story = [
        Paragraph("Gabriel Oliveira", name_style),
        Spacer(1, 1),
        Paragraph("BACKEND-FOCUSED FULL-STACK DEVELOPER", title_style),
        Spacer(1, 2),
        Paragraph(contact, contact_style),
        Spacer(1, 9),
        Paragraph(
            "Full-stack developer with stronger backend experience building APIs, automations and data-processing systems. "
            "Experienced with financial reconciliation, large-file imports, spreadsheet workflows, CNAB generation, portal automation "
            "and PDF extraction, and with shipping Windows desktop software end to end. Based in Brazil and open to remote "
            "international teams.",
            summary_style,
        ),
        Paragraph("TECHNICAL SKILLS", section_style),
        skill("Backend", "Node.js, TypeScript, JavaScript, PHP, Laravel, C#, .NET and REST APIs"),
        skill("Frontend", "React, React Native and responsive web and mobile interfaces"),
        skill("Desktop", "C# and .NET Windows apps, WinForms, Win32 APIs, FFmpeg and NSIS installers"),
        skill("Data", "MySQL, CSV and Excel processing, PDF extraction and CNAB workflows"),
        skill("Cloud and Tools", "AWS, S3, Lambda, API Gateway, CloudWatch, DynamoDB, Docker, Terraform, GitHub Actions and Git"),
        Paragraph("PROFESSIONAL EXPERIENCE", section_style),
        *entry("Full-Stack Developer", "South Wind Solution", "2022 - Present", [
            "Build and maintain web and mobile applications, integrate REST APIs, resolve production issues and improve responsive user experiences.",
            "Translate product and operational requirements into practical software across backend, frontend and mobile environments.",
        ]),
        *entry("Cloud Infrastructure Developer", "Contract Project", "2023", [
            "Developed infrastructure with Terraform and AWS, connecting TypeScript Lambdas, API Gateway, CloudWatch and DynamoDB.",
        ]),
        *entry("React Native Developer", "Freelance", "2023 - Present", [
            "Delivered a new flow for a banking application and resolved compatibility issues across Android devices and iOS.",
        ]),
        Paragraph("SELECTED PROJECTS", section_style),
        *entry("Prism Review", "Open Source", "2026", [
            "Built a deterministic GitHub Action that reviews pull requests for missing tests, large diffs, dependency changes and security-sensitive files before human review.",
            "Designed a safe execution model with minimal permissions, unit-tested rules, fixture-based analysis and a single upserted pull-request report.",
        ], "https://github.com/gabrielolvv/prism-review", "github.com/gabrielolvv/prism-review"),
        *entry("Ghostclip", "Open Source", "2026", [
            "Built an instant replay recorder for Windows in C# and .NET that keeps the last minute of gameplay and saves it on a hotkey, with no DLL injection, render hooks or global keyboard hook.",
            "Designed a two-process architecture: a supervised headless worker drives FFmpeg with GPU hardware encoding and restarts on failure without losing the on-disk buffer.",
        ], "https://github.com/gabrielolvv/ghostclip", "github.com/gabrielolvv/ghostclip"),
        *entry("MouseModes", "Open Source", "2026", [
            "Built a Windows tray app in C# that switches mouse and power settings between Performance and Everyday modes, manually, by global hotkey or automatically when a game launches.",
            "Shipped a per-user installer with self-updates verified against the release SHA-256, restoring every changed setting on exit or after a crash.",
        ], "https://gabrielolvv.github.io/mousemodes/", "gabrielolvv.github.io/mousemodes"),
        Paragraph("EDUCATION", section_style),
        *entry("Technology Degree in Systems Analysis and Development", "University of Fortaleza", "2021 - 2023", []),
    ]

    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=MARGIN - FRAME_PADDING,
        rightMargin=MARGIN - FRAME_PADDING,
        topMargin=40,
        bottomMargin=40,
        title="Gabriel Oliveira Resume",
        author="Gabriel Oliveira",
        subject="Backend-focused full-stack developer resume",
        creator="",
    )
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    build()
    print(f"Wrote {OUTPUT}")
