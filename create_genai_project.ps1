# Create root folder
New-Item -ItemType Directory -Force -Path "genai_project" | Out-Null
Set-Location "genai_project"

Write-Host "Creating top-level folders..."
New-Item -ItemType Directory -Force -Path ".vscode","00_learning","01_projects","02_sandboxes","config","envs","src_common","docs","scripts" | Out-Null

Write-Host "Creating env files placeholders..."
New-Item -ItemType File -Force -Path "envs/.env.dev","envs/.env.uat","envs/.env.prod" | Out-Null

Write-Host "Creating learning topic folders..."
$learningFolders = @(
  "00_learning/00_setup",
  "00_learning/01_llm_basics",
  "00_learning/02_prompt_engineering",
  "00_learning/03_embeddings_and_vectorstores",
  "00_learning/04_rag_fundamentals",
  "00_learning/05_langchain_core",
  "00_learning/06_streamlit_ui",
  "00_learning/07_fastapi_and_apis",
  "00_learning/08_agents_and_tools",
  "00_learning/09_eval_and_observability",
  "00_learning/10_advanced_topics",
  "00_learning/11_mini_projects",
  "00_learning/utils"
)
$learningFolders | ForEach-Object { New-Item -ItemType Directory -Force -Path $_ | Out-Null }

Write-Host "Creating example project skeleton..."
$projRoot = "01_projects/customer_support_bot"
$projFolders = @(
  "$projRoot/src/app_streamlit",
  "$projRoot/src/app_api",
  "$projRoot/src/utils",
  "$projRoot/notebooks",
  "$projRoot/config",
  "$projRoot/data/raw",
  "$projRoot/data/processed",
  "$projRoot/data/embeddings",
  "$projRoot/logs",
  "$projRoot/infra/k8s",
  "$projRoot/tests"
)
$projFolders | ForEach-Object { New-Item -ItemType Directory -Force -Path $_ | Out-Null }

New-Item -ItemType File -Force -Path "$projRoot/README.md","$projRoot/requirements.txt","$projRoot/.env.dev_example" | Out-Null

Write-Host "Creating src_common utilities placeholders..."
$commonFiles = @(
  "src_common/__init__.py",
  "src_common/openai_client.py",
  "src_common/embeddings_client.py",
  "src_common/config_loader.py",
  "src_common/logging_setup.py",
  "src_common/rag_base.py",
  "src_common/file_loader.py",
  "src_common/text_preprocess.py",
  "src_common/eval_utils.py"
)
$commonFiles | ForEach-Object { New-Item -ItemType File -Force -Path $_ | Out-Null }

Write-Host "Creating config placeholders..."
@"
default_model: gpt-4o-mini

models:
  gpt-4o-mini:
    provider: openai
    name: gpt-4o-mini
    max_tokens: 1024
"@ | Set-Content "config/models.yaml"

@"
default: chroma

chroma:
  persist_directory: ./data/embeddings/dev/
"@ | Set-Content "config/vector_db.yaml"

@"
version: 1
disable_existing_loggers: False
"@ | Set-Content "config/logging.yaml"

"app_name: genai_project" | Set-Content "config/app.yaml"

Write-Host "Creating docs placeholders..."
@"
# Environment Setup

- Create virtual environment
- Install dependencies from requirements.txt
- Set APP_ENV=dev|uat|prod and matching .env file in envs/
"@ | Set-Content "docs/environment_setup.md"

@"
# Architecture Overview

High-level: User -> LLM -> Vector DB -> Response -> UI
"@ | Set-Content "docs/architecture_overview.md"

@"
# Naming Conventions

- snake_case for Python files
- lower_snake_case for folders
- UpperCamelCase for classes
"@ | Set-Content "docs/naming_conventions.md"

Write-Host "Creating top-level files..."
@"
# genai_project

Central workspace for:
- GenAI learning (LLMs, RAG, agents, UI)
- Real-world GenAI projects
- Dev / UAT / Prod ready architecture
"@ | Set-Content "README.md"

"# Core GenAI dependencies will be listed here." | Set-Content "requirements.txt"

@"
name: genai_env
dependencies:
  - python=3.11
  - pip
  - pip:
      - -r requirements.txt
"@ | Set-Content "environment.yml"

@"
# Python
__pycache__/
*.pyc
*.pyo

# Environments
env/
venv/
.genai_env/
.env
envs/.env.*

# Data & logs
data/
logs/
*.log

# Jupyter
.ipynb_checkpoints/

# OS
.DS_Store
"@ | Set-Content ".gitignore"

Write-Host "Done! genai_project structure created."
