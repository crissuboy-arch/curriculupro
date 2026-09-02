# Deploy - CV Remix PRO

## Pre-requisitos

- Conta no Vercel (vercel.com)
- NVIDIA API Key (NVIDIA NIM)
- Git instalado
- Repositorio no GitHub

## Passo 1: Preparar Repositorio

```bash
cd curriculupro
git init
git remote add origin https://github.com/crissuboy-arch/curriculupro.git
git add .
git commit -m "feat: initial standalone CV Remix PRO"
git push -u origin main
```

## Passo 2: Conectar no Vercel

1. Acesse vercel.com/new
2. Importe o repositorio `crissuboy-arch/curriculupro`
3. Framework: **Other**
4. Build Command: (vazio)
5. Output Directory: (vazio)
6. Click **Deploy**

## Passo 3: Configurar Env Vars

No painel do Vercel > Settings > Environment Variables:

| Nome | Valor |
|------|-------|
| `NVIDIA_API_KEY` | `nvapi-sua-chave-aqui` |
| `APP_ID` | `cv-remix-pro` |

## Passo 4: Verificar

1. Acesse `https://curriculupro.vercel.app/static/cv-remix-pro.html`
2. Teste import de curriculo
3. Teste ferramentas IA
4. Teste export PDF/DOCX

## Dominio Personalizado (Opcional)

1. No Vercel > Settings > Domains
2. Adicione seu dominio
3. Configure DNS conforme instrucoes

## Troubleshooting

### Erro 500 na API
- Verifique se `NVIDIA_API_KEY` esta configurada
- Confirme que o modelo esta disponivel na NVIDIA NIM

### Frontend nao carrega
- Verifique se o arquivo esta em `/static/cv-remix-pro.html`
- Confirme os rewrites no `vercel.json`

### Export falha
- Verifique se `weasyprint` e `python-docx` estao no `requirements.txt`
- No Vercel, pode ser necessario configurar build overrides

## Variaveis de Ambiente

| Variavel | Obrigatorio | Descricao |
|----------|-------------|-----------|
| `NVIDIA_API_KEY` | Sim | Chave da NVIDIA NIM API |
| `APP_ID` | Nao | Default: `cv-remix-pro` |

## Status

- [x] Repositorio criado
- [x] Codigo commitado
- [ ] Deploy no Vercel (aguardando autorizacao)
