# Projeto-Analises-Descritivas

Pequeno projeto demonstrando como construir histogramas e calcular medidas de tendência central,
medidas separatrizes (quartis) e de dispersão (desvio padrão, IQR).

O repositório contém um script Python pronto para rodar um exemplo localmente.

## Conteúdo
- \`analise_descritiva.py\` — script principal (gera dados de exemplo, calcula estatísticas e salva histograma).
- \`requirements.txt\` — dependências para instalar.
- \`dados/exemplo.csv\` — será gerado automaticamente pelo script se não existir.
- \`outputs/histograma.png\` — arquivo gerado com o histograma.

## Requisitos
- Python 3.9+ recomendado
- pip

## Como rodar (passo a passo)
1. Clonar o repositório (se ainda não fez):
\`\`\`bash
git clone https://github.com/marianycoelho/Projeto-Analises-Descritivas.git
cd Projeto-Analises-Descritivas
\`\`\`

2. Criar e ativar um ambiente virtual:
\`\`\`bash
python3 -m venv .venv
source .venv/bin/activate
\`\`\`

3. Instalar dependências:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. Executar o script (gera dados de exemplo se necessário):
\`\`\`bash
python analise_descritiva.py
\`\`\`

5. Executar com um CSV próprio:
\`\`\`bash
python analise_descritiva.py --input caminhos/meu_arquivo.csv --output outputs/meu_histograma.png
\`\`\`

## Resultado
- Estatísticas serão impressas no terminal.
- Histograma salvo em \`outputs/histograma.png\`.

## Git — adicionar/commitar/push
Após criar/alterar os arquivos locais, rode:
\`\`\`bash
git add requirements.txt analise_descritiva.py README.md
git commit -m "Adicionar script de análise descritiva e README"
git push origin main
\`\`\`

## Fixar (pin) este repositório no seu perfil GitHub
- Via interface web:
  1. Vá ao seu perfil no GitHub.
  2. Clique em "Customize your pins" (ou "Customize" na seção Pinned repositories).
  3. Selecione \`Projeto-Analises-Descritivas\` e salve.

- Via API (opcional/automatizado): é possível usar a GraphQL API do GitHub para \`pinRepository\` — requer token com scopes apropriados.

## Licença
Adicione uma licença se desejar (ex.: MIT).
