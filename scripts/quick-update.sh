#!/bin/bash
# Script rápido para atualizar Resume + Gerar PDFs + Fazer Commit

set -e

echo "================================"
echo "🚀 Quick Update Script"
echo "================================"
echo ""

# Cores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Step 1: Gerar PDFs
echo -e "${BLUE}Step 1: Gerando PDFs...${NC}"
python3 scripts/generate-pdfs.py
echo ""

# Step 2: Mostrar status git
echo -e "${BLUE}Step 2: Status do Git${NC}"
echo ""
git status --short
echo ""

# Step 3: Pedir confirmação
echo -e "${YELLOW}Deseja fazer commit das mudanças? (s/n)${NC}"
read -r -n1 response
echo ""

if [[ "$response" == "s" || "$response" == "S" ]]; then
    echo ""
    echo -e "${BLUE}Digite a mensagem de commit:${NC}"
    read -r commit_msg
    
    ./scripts/ensure-not-on-main.sh
    git add -A
    git commit -m "docs: $commit_msg"
    
    echo ""
    echo -e "${GREEN}✅ Commit realizado!${NC}"
    echo -e "${BLUE}Histórico:${NC}"
    git log --oneline -5
else
    echo -e "${YELLOW}Commit cancelado.${NC}"
    echo "Para fazer commit depois: git add -A && git commit -m 'sua mensagem'"
fi

echo ""
echo -e "${GREEN}================================${NC}"
echo -e "${GREEN}✨ Feito!${NC}"
echo -e "${GREEN}================================${NC}"
