#!/usr/bin/env bash
set -euo pipefail
OWNER="${1:-marianycoelho}"

REPO="${2:-Projeto-Analises-Descritivas}"
PROJECT_NAME="Planejamento - Projeto Analises Descritivas"
PROJECT_BODY="Quadro de tarefas e milestones iniciais para o projeto."
OPEN_IN_BROWSER=true

function check_gh() {
  if ! command -v gh >/dev/null 2>&1; then
    echo "[erro] 'gh' (GitHub CLI) não encontrado. Instale e autentique com 'gh auth login'." >&2
    exit 1
  fi
}

function confirm() {
  echo "Vai criar um Project no repositório: ${OWNER}/${REPO}"
  echo "Project: ${PROJECT_NAME}"
  read -rp "Continuar? [y/N]: " yn
  case "$yn" in [Yy]* ) ;; * ) echo "Cancelado."; exit 0 ;; esac
}

function create_project() {
  echo "[info] Criando Project..."
  gh project create --repo "${OWNER}/${REPO}" --name "${PROJECT_NAME}" --body "${PROJECT_BODY}" >/dev/null
  echo "[ok] Project criado."
}

function create_issues() {
  echo "[info] Criando issues iniciais..."
  gh issue create --repo "${OWNER}/${REPO}" --title "Adicionar LICENSE (MIT)" --body "Adicionar arquivo LICENSE (MIT) ao repositório." --assignee @me >/dev/null || true
  gh issue create --repo "${OWNER}/${REPO}" --title "Adicionar .gitignore" --body "Adicionar .gitignore com .venv, outputs, __pycache__." >/dev/null || true
  gh issue create --repo "${OWNER}/${REPO}" --title "Testar analise_descritiva.py" --body "Criar venv, instalar dependências e rodar o script analise_descritiva.py para validar." >/dev/null || true
  echo "[ok] Issues criadas."
}

function open_project() {
  gh project view --repo "${OWNER}/${REPO}" --web || true
}

check_gh
confirm
create_project
create_issues
if [ "${OPEN_IN_BROWSER}" = true ]; then
  open_project
fi
echo "[feito] Projeto criado e issues adicionadas."
