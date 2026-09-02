# CV Remix PRO

Consultor de carreira com IA para criar, melhorar e adaptar curriculos profissionais. Exporta PDF e DOCX.

## Funcionalidades

- Importar curriculo (PDF, DOCX, TXT)
- Melhoria com IA (gramatica, ATS, formatacao)
- Adaptacao para cargo especifico
- Adaptacao para mercado portugues/europeu
- Traducao para 7 idiomas (PT-PT, PT-BR, EN, ES, FR, DE, IT)
- Carta de conducao (13 categorias)
- Disponibilidade e autorizacao de trabalho
- Exportacao PDF e DOCX

## Inicio Rapido

```bash
pip install -r requirements.txt
cp .env.example .env
# Edite .env com sua NVIDIA_API_KEY
python server.py
```

Abra `http://localhost:8000/static/cv-remix-pro.html`

## Deploy (Vercel)

```bash
vercel deploy
```

Veja `docs/DEPLOY.md` para detalhes.

## Documentacao

- `docs/REMIX-GUIDE.md` - Guia de uso do editor
- `docs/ARCHITECTURE.md` - Arquitetura do projeto
- `docs/DEPLOY.md` - Deploy no Vercel
- `docs/API.md` - Referencia da API

## Estrutura

```
curriculupro/
  app_core.py          # Backend FastAPI
  config.py            # Configuracoes
  server.py            # Servidor local
  api/index.py         # Entry point Vercel
  static/              # Frontend HTML
  configs/             # Config JSON do app
  skills/              # System prompts IA
  assets/              # Assets estaticos
  docs/                # Documentacao
  examples/            # Exemplos de CV
  requirements.txt     # Dependencias
  vercel.json          # Config Vercel
  .env.example         # Template env
```

## Licenca

Uso interno. Nao redistribuir.
