# 📄 Guia de Geração de PDFs & Manutenção de Portfolio

## 🎯 Objetivo

Automatizar a geração de PDFs profissionais (Resume em EN-US e Currículo em PT-BR) a partir de arquivos Markdown. Sempre pronto para enviar para recrutadores.

---

## 📂 Estrutura de Arquivos

```
resume/
├── README.md                                # Hub central
├── resume-LEANDRO-KHALIL.md                # CV em Inglês (EN-US)
├── curriculo-LEANDRO-KHALIL-pt-BR.md       # CV em Português (PT-BR)
├── REMOTE-JOBS.md                          # Opções de engajamento (EN-US)
├── FREELANCER-PROJECTS.md                  # Portfolio freelancer (EN-US)
├── CHANGELOG.md                            # Histórico de atualizações
├── Makefile                                # Automação (make pdf, etc)
│
├── scripts/
│   └── generate-pdfs.py                    # Script Python para gerar PDFs
│
├── pdfs/                                   # 📁 PDFs gerados (ignore no git)
│   ├── RESUME-LEANDRO-KHALIL-en-US.pdf
│   ├── CURRICULO-LEANDRO-KHALIL-pt-BR.pdf
│   ├── REMOTE-JOBS-en-US.pdf
│   └── FREELANCER-PROJECTS-en-US.pdf
│
└── .gitignore                              # Ignora PDFs do versionamento
```

---

## 🔄 Fluxo de Trabalho (Como Usar)

### Step 1️⃣: Editar Arquivos Markdown

Edite qualquer um dos `.md` files:
- **resume-LEANDRO-KHALIL.md** — CV técnico em inglês
- **curriculo-LEANDRO-KHALIL-pt-BR.md** — CV em português
- **REMOTE-JOBS.md** — Opcões de engajamento para recrutadores
- **FREELANCER-PROJECTS.md** — Tipos de projetos freelancer

```bash
# Exemplo: editar o resume em inglês
code resume-LEANDRO-KHALIL.md

# Salve o arquivo (Ctrl+S no editor)
```

### Step 2️⃣: Gerar PDFs Atualizados

```bash
# Opção A: Usar o Makefile (recomendado)
make pdf

# Opção B: Rodar script Python diretamente
python3 scripts/generate-pdfs.py
```

**Resultado esperado:**
```
============================================================
📄 Gerando PDFs para Resume & Currículo
============================================================
✅ PDF gerado: pdfs/RESUME-LEANDRO-KHALIL-en-US.pdf
✅ PDF gerado: pdfs/CURRICULO-LEANDRO-KHALIL-pt-BR.pdf
✅ PDF gerado: pdfs/REMOTE-JOBS-en-US.pdf
✅ PDF gerado: pdfs/FREELANCER-PROJECTS-en-US.pdf
============================================================
✨ Concluído: 4/4 PDFs gerados
📁 Localização: pdfs/
============================================================
```

### Step 3️⃣: Atualizar CHANGELOG

```bash
# Adicione a mudança ao CHANGELOG
make update-changelog

# Ou edite manualmente: CHANGELOG.md
```

**Formato esperado no CHANGELOG:**
```markdown
## [1.2.0] - 2026-06-12

### Added
- ✅ Nova seção sobre consulting em REMOTE-JOBS.md

### Changed
- 📝 Atualizado preços em FREELANCER-PROJECTS.md

### Improved
- 🎯 Melhor estrutura de pitches por tipo de vaga
```

### Step 4️⃣: Fazer Commit no Git

```bash
# Opção A: Automático com Makefile
make git-commit

# Opção B: Manual
git add -A
git commit -m "docs: atualizar resume e gerar PDFs

- Adicionar experiência recente
- Atualizar stack técnico
- Gerar novos PDFs"
```

---

## 📊 Comandos Disponíveis

| Comando | O que faz |
|---------|-----------|
| `make help` | Mostra este help |
| `make pdf` | Gera todos os 4 PDFs |
| `make clean` | Remove PDFs antigos |
| `make update-changelog` | Adiciona entrada ao CHANGELOG |
| `make git-commit` | Faz commit automático |
| `make view-pdfs` | Lista PDFs gerados |

---

## 🎯 Checklist para Atualizar

Sempre que atualizar o portfolio:

- [ ] Editar arquivo `.md` (resume, currículo, ou outro)
- [ ] Rodar `make pdf` para gerar PDFs
- [ ] Abrir PDF no navegador e validar formatação
- [ ] Atualizar `CHANGELOG.md` com mudanças
- [ ] Fazer `git add` + `git commit`
- [ ] Fazer `git push` para enviar para GitHub

---

## 💡 Dicas & Boas Práticas

### ✅ Faça:
- **Mantenha PT-BR para currículo** — Use o `curriculo-LEANDRO-KHALIL-pt-BR.md`
- **Mantenha EN-US para resume** — Use o `resume-LEANDRO-KHALIL.md`
- **Atualize CHANGELOG após cada mudança** — Ajuda a rastrear histórico
- **Valide PDFs antes de enviar** — Abra no navegador e revise
- **Use versionamento semântico** — v1.0.0, v1.1.0, v2.0.0

### ❌ Não faça:
- **Não edite PDFs diretamente** — Sempre edite os `.md` e regenere
- **Não misture PT-BR com EN-US** — Mantenha separado
- **Não comite PDFs antigos** — Adicione `pdfs/` ao `.gitignore`
- **Não ignore o CHANGELOG** — É importante para tracking

---

## 🔧 Troubleshooting

### ❌ Erro: "Python3 not found"
```bash
sudo apt-get install python3 python3-pip
```

### ❌ Erro: "Module weasyprint not found"
```bash
python3 -m pip install --user weasyprint markdown2
```

### ❌ PDFs vazios ou formatação ruim
1. Verifique sintaxe Markdown (headers com `#`, listas com `-`)
2. Regenere: `make clean && make pdf`
3. Abra em navegador para validar

### ❌ Git recusa fazer commit
```bash
git config user.email "khallipdev@gmail.com"
git config user.name "Leandro Khalil"
git add . && git commit -m "docs: atualização"
```

---

## 📤 Como Enviar para Recrutadores

### Via Email

```
Assunto: Resumé & Portfolio - Leandro Khalil (Senior C# Developer)

Olá [Recruiter],

Segue em anexo meu resume e portfolio profissional:

📄 Resume (EN-US): RESUME-LEANDRO-KHALIL-en-US.pdf
📄 Remote Jobs & Options: REMOTE-JOBS-en-US.pdf
📄 Freelancer Portfolio: FREELANCER-PROJECTS-en-US.pdf

Para PT-BR:
📄 Currículo (PT-BR): CURRICULO-LEANDRO-KHALIL-pt-BR.pdf

Fico disponível para discussão sobre oportunidades remotas ou projetos freelancer.

Att,
Leandro
khallipdev@gmail.com
+55 (62) 99880-8389
```

### Via LinkedIn
- Adicione link do GitHub com este portfolio
- Compartilhe o README.md como post
- Marque keywords: #CSharp #NET #SeniorDeveloper #RemoteWork

### Via Plataformas
- **Toptal:** Upload do RESUME-LEANDRO-KHALIL-en-US.pdf
- **Gun.io:** Upload do RESUME-LEANDRO-KHALIL-en-US.pdf
- **LinkedIn:** Link para repositório GitHub

---

## 📅 Ciclo de Atualização Recomendado

| Frequência | O que atualizar |
|-----------|-----------------|
| **Semanal** | Currículo/Resume (quando termina projeto) |
| **Mensal** | CHANGELOG com progresso |
| **Trimestral** | Atualizar preços em FREELANCER-PROJECTS.md |
| **Anual** | Restrurar seções principais do Resume |

---

## 🔗 Referências

- [Markdown Syntax](https://www.markdownguide.org/basic-syntax/)
- [Make Tutorial](https://www.gnu.org/software/make/manual/)
- [WeasyPrint Docs](https://weasyprint.org/)

---

## 📞 Suporte

Se tiver problemas com geração de PDFs:
- Verifique sintaxe Markdown
- Rode `make clean && make pdf` para regenerar
- Valide PDF aberto no navegador

Para questions sobre portfolio:
- Email: khallipdev@gmail.com
- WhatsApp: +55 (62) 99880-8389

---

*Guia atualizado: 2026-06-12*
