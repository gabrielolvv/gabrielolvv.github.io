# gabrielolvv.github.io

Portfólio de Gabriel Oliveira, desenvolvedor full-stack com foco em backend.

**Site:** https://gabrielolvv.github.io/

## Estrutura

Site estático, sem etapa de build: HTML, CSS e JavaScript escritos à mão, com
alternância entre inglês e português.

```
dist/
  index.html            página principal
  prism-review/         estudo de caso do Prism Review
  404.html              página de rota não encontrada
  og.jpg                imagem de compartilhamento (1200×630)
  resume.pdf            currículo
  robots.txt, sitemap.xml
```

## Rodar localmente

```bash
python -m http.server 8000 --directory dist
```

Depois abra http://localhost:8000.

## Deploy

Todo push na `main` publica a pasta `dist/` no GitHub Pages pelo workflow
[`.github/workflows/pages.yml`](.github/workflows/pages.yml).
