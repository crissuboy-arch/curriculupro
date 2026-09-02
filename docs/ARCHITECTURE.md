# Arquitetura - CV Remix PRO

## Visao Geral

Aplicacao full-stack com backend Python (FastAPI) e frontend SPA (HTML vanilla).

## Backend

### app_core.py
- FastAPI com endpoints REST
- Integracao NVIDIA NIM API (OpenAI-compatible SDK)
- Parse de PDF (pypdf), DOCX (python-docx), TXT
- Exportacao PDF (weasyprint) e DOCX (python-docx)
- CORS configurado para desenvolvimento

### config.py
- Carrega configuracao de `configs/cv-remix-pro.json`
- Cache de configuracoes em memoria
- Suporte a multiplos apps via `APP_ID`
- Default: `cv-remix-pro`

### server.py
- Servidor local para desenvolvimento
- Porta 8000, auto-reload

### api/index.py
- Entry point para Vercel serverless
- Invoca `app_core.app` (FastAPI)

## Frontend

### static/cv-remix-pro.html
- SPA unica (~66KB)
- Vanilla HTML/CSS/JS, sem frameworks
- Import via drag-and-drop ou file picker
- Barra de ferramentas IA
- Exportacao PDF/DOCX
- Idioma selection (7 opcoes)
- Compare mode (antes/depois)

## Configuracao

### configs/cv-remix-pro.json
- Branding (cores, icones, nomes)
- System prompts por ferramenta
- Modelos IA disponiveis
- Sidebar e action buttons

### skills/cv-remix-pro.md
- System prompt para IA
- Regras: nunca inventar dados
- Campos do curriculo
- Capacidades (melhoria, traducao, adaptacao)

## IA

- **Provider**: NVIDIA NIM API
- **Endpoint**: `https://integrate.api.nvidia.com/v1`
- **Modelo default**: `meta/llama-3.1-70b-instruct`
- **Auth**: `NVIDIA_API_KEY` via env var
- **SDK**: `openai` (compatible)

## Fluxo de Dados

```
Frontend (HTML)
  -> POST /api/parse (arquivo)
  -> POST /api/enhance (texto + tool)
  -> POST /api/translate (texto + idioma)
  -> POST /api/adapt (texto + cargo)
  -> POST /api/export/pdf (JSON -> PDF)
  -> POST /api/export/docx (JSON -> DOCX)
```

## Dependencias

- fastapi, uvicorn
- openai (NVIDIA NIM)
- python-docx (DOCX)
- pypdf (PDF parse)
- weasyprint (PDF export)
- python-dotenv
- requests, beautifulsoup4

## Deploy

- **Plataforma**: Vercel (serverless)
- **Entry**: `api/index.py`
- **Rewrites**: `/api/*` -> `api/index.py`, `/static/*` -> mantido
- **Env vars**: `NVIDIA_API_KEY`, `APP_ID=cv-remix-pro`
