.PHONY: help pdf pdf-watch clean update-changelog install-hooks git-commit

help:
	@echo "================================"
	@echo "📄 Resume & Portfolio Management"
	@echo "================================"
	@echo ""
	@echo "Comandos disponíveis:"
	@echo ""
	@echo "  make pdf              - Gera todos os PDFs (resume, currículo, freelancer)"
	@echo "  make clean            - Remove PDFs antigos"
	@echo "  make update-changelog - Atualiza CHANGELOG.md com data e versão"
	@echo "  make install-hooks    - Instala o hook local de proteção de commit"
	@echo "  make git-commit       - Faz commit de todas as mudanças (git add + commit)"
	@echo ""
	@echo "Fluxo recomendado para atualizações:"
	@echo "  1. Edite os arquivos .md (resume, currículo, etc)"
	@echo "  2. make pdf              # Gera PDFs atualizados"
	@echo "  3. make update-changelog # Adiciona entrada no CHANGELOG"
	@echo "  4. make git-commit       # Faz commit de tudo"
	@echo ""

pdf:
	@echo "📄 Gerando PDFs..."
	@python3 scripts/generate-pdfs.py
	@echo ""
	@echo "✅ PDFs disponíveis em: ./pdfs/"

clean:
	@echo "🗑️  Removendo PDFs antigos..."
	@rm -rf pdfs/*.pdf
	@echo "✅ Feito"

update-changelog:
	@echo "📝 Atualizando CHANGELOG.md..."
	@echo ""
	@echo "Digite a descrição das mudanças (tecle Enter quando terminar):"
	@read changes; \
	echo "## [Atualizado] - $$(date +%Y-%m-%d)" >> CHANGELOG.md; \
	echo "" >> CHANGELOG.md; \
	echo "### Mudanças" >> CHANGELOG.md; \
	echo "$$changes" >> CHANGELOG.md; \
	echo "" >> CHANGELOG.md; \
	git add CHANGELOG.md
	@echo "✅ CHANGELOG atualizado"

install-hooks:
	@echo "🔧 Instalando hooks locais..."
	@chmod +x scripts/ensure-not-on-main.sh .githooks/pre-commit
	@git config core.hooksPath .githooks
	@echo "✅ Hooks instalados em .githooks"

git-commit:
	@echo "📦 Preparando commit..."
	@./scripts/ensure-not-on-main.sh
	@git add -A
	@echo ""
	@echo "Arquivos prontos para commit:"
	@git status --short
	@echo ""
	@echo "Digite mensagem de commit:"
	@read msg; \
	git commit -m "docs: $$msg" --allow-empty
	@echo ""
	@echo "✅ Commit realizado. Verifique com: git log --oneline -5"

view-pdfs:
	@echo "📂 PDFs disponíveis:"
	@ls -lh pdfs/
