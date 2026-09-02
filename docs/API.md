# API - CV Remix PRO

Base URL: `http://localhost:8000` (local) ou `https://curriculupro.vercel.app` (producao)

## Endpoints

### Health Check

```
GET /api/health
```

Response:
```json
{
  "status": "ok",
  "app": "cv-remix-pro"
}
```

### List Configs

```
GET /api/configs
```

Response:
```json
[
  {
    "app_id": "cv-remix-pro",
    "app_name": "CV Remix PRO",
    "short_name": "CV Remix",
    "description": "...",
    "icon": "...",
    "color": "#2563EB",
    "assistant_name": "..."
  }
]
```

### Get Config

```
GET /api/config
```

Response: Configuracao completa do app.

### Parse CV

```
POST /api/parse
Content-Type: multipart/form-data
```

Body:
- `file`: Arquivo PDF, DOCX ou TXT

Response:
```json
{
  "success": true,
  "data": {
    "personal": {
      "name": "...",
      "email": "...",
      "phone": "...",
      "location": "...",
      "country": "...",
      "nationality": "...",
      "birth_date": "...",
      "linkedin": "...",
      "portfolio": "..."
    },
    "summary": "...",
    "experience": [...],
    "education": [...],
    "skills": {
      "technical": [...],
      "personal": [...]
    },
    "languages": [...],
    "certifications": [...],
    "driving_license": {
      "has_license": true,
      "categories": ["B", "BE"],
      "own_vehicle": true
    },
    "availability": {
      "immediate": true,
      "shifts": false,
      "weekends": false,
      "travel": true,
      "relocation": false
    },
    "work_authorization": {
      "authorized": "sim",
      "permit_type": "..."
    },
    "target_job": "..."
  }
}
```

### Enhance CV

```
POST /api/enhance
Content-Type: application/json
```

Body:
```json
{
  "cv_text": "Texto do curriculo...",
  "tool": "improve",
  "language": "pt-pt"
}
```

Tools disponiveis:
- `improve` - Melhoria geral
- `improve_all` - Todas as melhorias
- `grammar` - Correcao gramatical
- `ats` - Otimizacao ATS
- `adapt_pt` - Adaptar para Portugal
- `expand` - Expandir informacoes
- `summarize` - Resumir para 1 pagina

### Translate CV

```
POST /api/translate
Content-Type: application/json
```

Body:
```json
{
  "cv_text": "Texto do curriculo...",
  "target_language": "en"
}
```

Idiomas suportados: `pt-pt`, `pt-br`, `en`, `es`, `fr`, `de`, `it`

### Adapt CV

```
POST /api/adapt
Content-Type: application/json
```

Body:
```json
{
  "cv_text": "Texto do curriculo...",
  "target_job": "Analista de Dados"
}
```

### Export PDF

```
POST /api/export/pdf
Content-Type: application/json
```

Body:
```json
{
  "data": { ... },
  "language": "pt-pt"
}
```

Response: Arquivo PDF (application/pdf)

### Export DOCX

```
POST /api/export/docx
Content-Type: application/json
```

Body:
```json
{
  "data": { ... },
  "language": "pt-pt"
}
```

Response: Arquivo DOCX (application/vnd.openxmlformats-officedocument.wordprocessingml.document)
