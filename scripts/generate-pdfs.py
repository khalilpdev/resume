#!/usr/bin/env python3
"""
Script para gerar PDFs a partir de arquivos Markdown.
Suporta PT-BR e EN-US com CSS customizado para melhor formatação.
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from weasyprint import HTML, CSS
from io import StringIO

# Define base path
BASE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = BASE_DIR / "pdfs"
OUTPUT_DIR.mkdir(exist_ok=True)

# CSS customizado para melhor formatação
CUSTOM_CSS = """
@page {
    size: A4;
    margin: 0.8in 0.8in 0.8in 0.8in;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #333;
}

h1 {
    font-size: 18pt;
    font-weight: bold;
    margin: 0 0 0.2em 0;
    color: #1a1a1a;
    border-bottom: 2px solid #0066cc;
    padding-bottom: 0.3em;
}

h2 {
    font-size: 13pt;
    font-weight: bold;
    margin: 1.2em 0 0.4em 0;
    color: #0066cc;
    page-break-after: avoid;
}

h3 {
    font-size: 11.5pt;
    font-weight: bold;
    margin: 0.8em 0 0.2em 0;
    color: #333;
    page-break-after: avoid;
}

h4 {
    font-size: 11pt;
    font-weight: bold;
    margin: 0.5em 0 0.2em 0;
}

p {
    margin: 0.4em 0;
}

em, strong {
    font-weight: 600;
}

a {
    color: #0066cc;
    text-decoration: none;
}

ul, ol {
    margin: 0.4em 0;
    padding-left: 1.5em;
}

li {
    margin: 0.2em 0;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 0.6em 0;
    font-size: 10pt;
}

th, td {
    border: 1px solid #ddd;
    padding: 0.4em 0.5em;
    text-align: left;
}

th {
    background-color: #f0f0f0;
    font-weight: bold;
}

hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 1em 0;
}

code {
    background-color: #f5f5f5;
    padding: 0.2em 0.4em;
    border-radius: 3px;
    font-family: 'Courier New', monospace;
    font-size: 10pt;
}

blockquote {
    border-left: 4px solid #0066cc;
    padding-left: 1em;
    margin-left: 0;
    color: #666;
    font-style: italic;
}

@media print {
    a {
        text-decoration: none;
    }
    h2 {
        page-break-before: avoid;
    }
}
"""

def markdown_to_html(md_content):
    """Converte Markdown para HTML simples (sem biblioteca markdown)."""
    html = md_content
    
    # Conversões básicas markdown → HTML
    lines = html.split('\n')
    result = []
    in_ul = False
    in_ol = False
    
    for line in lines:
        # Headers
        if line.startswith('# '):
            result.append(f'<h1>{line[2:].strip()}</h1>')
        elif line.startswith('## '):
            result.append(f'<h2>{line[3:].strip()}</h2>')
        elif line.startswith('### '):
            result.append(f'<h3>{line[4:].strip()}</h3>')
        elif line.startswith('#### '):
            result.append(f'<h4>{line[5:].strip()}</h4>')
        # Listas
        elif line.startswith('- '):
            if not in_ul:
                result.append('<ul>')
                in_ul = True
            result.append(f'<li>{line[2:].strip()}</li>')
        elif line.startswith('* '):
            if not in_ul:
                result.append('<ul>')
                in_ul = True
            result.append(f'<li>{line[2:].strip()}</li>')
        # Tabelas (básico)
        elif '|' in line and line.count('|') >= 2:
            result.append('<table><tr>' + ''.join(f'<td>{cell.strip()}</td>' 
                         for cell in line.split('|')[1:-1]) + '</tr></table>')
        # Linhas horizontais
        elif line.strip() in ['---', '***', '___']:
            result.append('<hr/>')
        # Parágrafos normais
        elif line.strip():
            if in_ul:
                result.append('</ul>')
                in_ul = False
            # Bold e Italic
            text = line.strip()
            text = text.replace('**', '<strong>', 1).replace('**', '</strong>')
            text = text.replace('*', '<em>', 1).replace('*', '</em>')
            text = text.replace('__', '<strong>', 1).replace('__', '</strong>')
            text = text.replace('_', '<em>', 1).replace('_', '</em>')
            result.append(f'<p>{text}</p>')
        else:
            if in_ul:
                result.append('</ul>')
                in_ul = False
    
    if in_ul:
        result.append('</ul>')
    
    return '\n'.join(result)

def generate_pdf(md_file, output_name=None, title="Document"):
    """
    Gera PDF a partir de arquivo Markdown.
    
    Args:
        md_file: Caminho do arquivo .md
        output_name: Nome do arquivo de saída (sem extensão)
        title: Título do documento
    """
    md_path = BASE_DIR / md_file
    
    if not md_path.exists():
        print(f"❌ Arquivo não encontrado: {md_path}")
        return False
    
    # Lê conteúdo do MD
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Converte para HTML
    html_content = markdown_to_html(md_content)
    
    # Envuelve em HTML completo
    full_html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>{CUSTOM_CSS}</style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Define nome do output
    if not output_name:
        output_name = md_path.stem
    
    output_path = OUTPUT_DIR / f"{output_name}.pdf"
    
    try:
        # Gera PDF com WeasyPrint
        HTML(string=full_html).write_pdf(
            str(output_path),
            zoom=1,
        )
        print(f"✅ PDF gerado: {output_path}")
        return True
    except Exception as e:
        print(f"❌ Erro ao gerar PDF: {e}")
        return False

def main():
    """Gera todos os PDFs necessários."""
    print("=" * 60)
    print("📄 Gerando PDFs para Resume & Currículo")
    print("=" * 60)
    
    # Define os documentos a gerar
    documents = [
        ("resume-LEANDRO-KHALIL.md", "RESUME-LEANDRO-KHALIL-en-US", "Leandro Khalil - Resume (EN-US)"),
        ("curriculo-LEANDRO-KHALIL-pt-BR.md", "CURRICULO-LEANDRO-KHALIL-pt-BR", "Leandro Khalil - Currículo (PT-BR)"),
        ("REMOTE-JOBS.md", "REMOTE-JOBS-en-US", "Remote Jobs & Freelancer Options (EN-US)"),
        ("FREELANCER-PROJECTS.md", "FREELANCER-PROJECTS-en-US", "Freelancer Projects Portfolio (EN-US)"),
    ]
    
    success_count = 0
    for md_file, output_name, title in documents:
        if generate_pdf(md_file, output_name, title):
            success_count += 1
    
    print("=" * 60)
    print(f"✨ Concluído: {success_count}/{len(documents)} PDFs gerados")
    print(f"📁 Localização: {OUTPUT_DIR}")
    print("=" * 60)
    
    return success_count == len(documents)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
