# Changelog

Histórico de atualizações no portfólio profissional de Leandro Khalil.

---

## 2026-06-18

### Repository Repositioning

* Introduced Resume-as-Code concept
* Updated README
* Refined professional positioning
* Increased focus on Full-Stack Development
* Reduced emphasis on management roles
* Highlighted international opportunities
* Added tracked git-hook guard for direct commits on main/master

---

## [1.3.0] - 2026-06-15 📊 Versões de Currículo v2 (Métricas) & v3 (Liderança)

### Added
- ✅ **Nova pasta `versions/v2`** contendo currículos voltados a métricas e impacto:
  - `resume-LEANDRO-KHALIL.md` (EN-US)
  - `curriculo-LEANDRO-KHALIL-pt-BR.md` (PT-BR)
  - Foco em resultados quantitativos de alta precisão (conforme regras Ágeis e ATS).
- ✅ **Nova pasta `versions/v3`** contendo currículos voltados a Liderança Estratégica e Arquitetura:
  - `resume-LEANDRO-KHALIL.md` (EN-US)
  - `curriculo-LEANDRO-KHALIL-pt-BR.md` (PT-BR)
  - Foco em gestão técnica (CTO/Lead Architect), alinhamento com executivos, design complexo de microsserviços (CQRS, Event Sourcing, DDD).

### Improved
- 🔄 **Otimização do .gitignore**: Corrigida a sintaxe de comentários na mesma linha de pastas ignoradas, assegurando que pastas temporárias e backups gerados localmente não poluam o controle de versão do Git.
- ⚙️ **Automação do Gerador de PDFs**: Atualizado o script `scripts/generate-pdfs.py` para compilar automaticamente as novas versões v2 e v3 para PDFs otimizados.

### Generated (Novos PDFs Prontos)
- 📄 `RESUME-LEANDRO-KHALIL-en-US-v2.pdf`
- 📄 `CURRICULO-LEANDRO-KHALIL-pt-BR-v2.pdf`
- 📄 `RESUME-LEANDRO-KHALIL-en-US-v3.pdf`
- 📄 `CURRICULO-LEANDRO-KHALIL-pt-BR-v3.pdf`

---

## [1.2.0] - 2026-06-12 🚀 Automação de PDFs & Versionamento PT-BR/EN-US

### Added
- ✅ **Script de Automação Python** (`scripts/generate-pdfs.py`)
  - Converte Markdown → PDF automaticamente
  - Suporta PT-BR e EN-US
  - CSS customizado para formatação profissional
  
- ✅ **curriculo-LEANDRO-KHALIL-pt-BR.md** — Versão em português do CV
  - Tradução completa do resume
  - Mantém especialidades técnicas
  - Pronto para enviar a recrutadores brasileiros
  
- ✅ **PDF-GENERATION-GUIDE.md** — Guia completo de uso
  - Fluxo de trabalho recomendado
  - Comandos disponíveis
  - Troubleshooting e dicas
  
- ✅ **Makefile** — Automação de comandos
  - `make pdf` — Gera todos os PDFs
  - `make clean` — Remove PDFs antigos
  - `make update-changelog` — Atualiza CHANGELOG
  - `make git-commit` — Faz commit automático
  
- ✅ **.gitignore** — Ignora PDFs do versionamento

### Changed
- 📝 README.md mantém referências atualizadas para todos documentos
- 🔄 PDFs agora gerados em pasta `pdfs/` separada

### Generated (PDFs Prontos para Enviar)
- 📄 `RESUME-LEANDRO-KHALIL-en-US.pdf` (26 KB)
- 📄 `CURRICULO-LEANDRO-KHALIL-pt-BR.pdf` (27 KB)
- 📄 `REMOTE-JOBS-en-US.pdf` (74 KB)
- 📄 `FREELANCER-PROJECTS-en-US.pdf` (91 KB)

### Improved
- 🎯 Sistema totalmente automatizado (editar .md → gerar PDF em 1 comando)
- 📊 Versionamento bidirecional PT-BR/EN-US
- 📞 Instruções claras para manutenção futura

---

## [1.1.0] - 2026-06-12

### Added
- ✅ **REMOTE-JOBS.md** — Documento com 3 opções de engajamento (Full-time, Freelancer, Consulting)
  - Template de email para recrutadores
  - Pitches customizados por tipo de vaga
  - Informações de salário esperado e preferências
  
- ✅ **FREELANCER-PROJECTS.md** — Portfolio de 6 tipos de projetos freelancer
  - Modernização de Legacy Systems
  - Integração ERP (SAP B1/S/4HANA)
  - SaaS MVPs
  - Data pipelines ETL
  - Performance audits
  - Technical leadership & mentoring
  - Tabela de preços referência
  
- ✅ **README.md atualizado** com estrutura clara
  - Seção "Se você está aqui porque..."
  - Links para documentos específicos
  - Quick overview de expertise
  - Métrica de experiência

### Changed
- 📝 README.md agora funciona como **hub central** para navegação

### Improved
- 🎯 Melhor organização de conteúdo por público (Recrutador vs Freelancer vs Cliente)
- 📊 Adicionado tabela de preços com ranges realistas
- 💬 Templates de pitch para diferentes tipos de vaga
- 📞 Informações de contato centralizadas

---

## [1.0.0] - Data inicial

### Base Structure
- ✅ **resume-LEANDRO-KHALIL.md** — CV técnico em inglês
  - 18+ anos de experiência documentados
  - 8 posições anteriores descritas
  - Stack técnico (C#, .NET, SQL, ERP)
  - Projetos-chave e achievements
  - Educação e formação

---

## 📝 Plano Futuro

### Próximas Versões

#### [1.2.0] - Portfolio de Casos de Uso
- [ ] Criar **CASE-STUDIES.md** com 3-5 cases reais (anonimizados)
  - Antes/depois de performance
  - Impacto em negócio
  - Tecnologias usadas
  
#### [1.3.0] - Materiais de Venda Avançados
- [ ] **ELEVATOR-PITCH.md** — Versões de 30s, 2min, 5min
- [ ] **FAQ-RECRUTADORES.md** — Respostas a perguntas comuns
- [ ] **TESTIMONIALS.md** — Feedback de clientes/colegas (opcional)

#### [1.4.0] - Blog/Articles
- [ ] Links para artigos técnicos publicados
- [ ] GitHub com projetos showcase (open-source)

#### [2.0.0] - Website Estático
- [ ] Versão HTML do portfolio (hospedado)
- [ ] Gerador de PDFs do CV em múltiplos idiomas
- [ ] Formulário de contato integrado

---

## 📊 Estatísticas do Repositório

| Métrica | Valor |
|---------|-------|
| **Documentos** | 5 arquivos (.md + .docx) |
| **Últimas Atualizações** | 2026-06-12 |
| **Commits** | 1+ |
| **Público-alvo** | Recrutadores, clientes, freelancers |

---

## 🔄 Como Usar Este Changelog

Sempre que **atualizar conteúdo**:

1. ✏️ Edite o documento relevante (REMOTE-JOBS.md, FREELANCER-PROJECTS.md, etc)
2. 📋 Adicione a mudança aqui no CHANGELOG.md
3. 🔖 Atualize a versão (MAJOR.MINOR.PATCH)
4. 📅 Coloque a data no formato YYYY-MM-DD
5. 🔗 Faça commit com mensagem descritiva

### Exemplo de Commit
```bash
git add .
git commit -m "docs: atualizar pitches e adicionar novo tipo de projeto

- Adicionar padrão de pitch para startups
- Expandir seção de preços em FREELANCER-PROJECTS
- Atualizar templates de email em REMOTE-JOBS

Versão: 1.1.1"
```

---

## 📞 Contato para Sugestões

Se tem feedback sobre o portfolio ou documentação:  
📧 **khallipdev@gmail.com**  
📱 **+55 (62) 99880-8389**

---

## 📜 Notas de Versão

### v1.1.0 Highlights
> Primeira versão completa com especialização em recrutamento e freelancer.
> Inclui 3 documentos principais + README refatorado.
> Pronto para distribuição em larga escala a recrutadores.

---

*Mantido por Leandro Khalil Peixoto*  
*Último atualizado: 2026-06-12*
