from pathlib import Path

def create_dirs(paths):
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)

def create_files(files):
    for file in files:
        file.parent.mkdir(parents=True, exist_ok=True)
        file.touch(exist_ok=True)

def write_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")

def main():
    project_root = Path("genai_project")
    project_root.mkdir(exist_ok=True)
    print("Project root created.")

    # Change working directory
    import os
    os.chdir(project_root)

    print("Creating top-level folders...")
    top_level_dirs = [
        Path(".vscode"),
        Path("00_learning"),
        Path("01_projects"),
        Path("02_sandboxes"),
        Path("config"),
        Path("envs"),
        Path("src_common"),
        Path("docs"),
        Path("scripts"),
    ]
    create_dirs(top_level_dirs)

    print("Creating env files placeholders...")
    env_files = [
        Path("envs/.env.dev"),
        Path("envs/.env.uat"),
        Path("envs/.env.prod"),
    ]
    create_files(env_files)

    print("Creating learning topic folders...")
    learning_dirs = [
        Path("00_learning/00_setup"),
        Path("00_learning/01_llm_basics"),
        Path("00_learning/02_prompt_engineering"),
        Path("00_learning/03_embeddings_and_vectorstores"),
        Path("00_learning/04_rag_fundamentals"),
        Path("00_learning/05_langchain_core"),
        Path("00_learning/06_streamlit_ui"),
        Path("00_learning/07_fastapi_and_apis"),
        Path("00_learning/08_agents_and_tools"),
        Path("00_learning/09_eval_and_observability"),
        Path("00_learning/10_advanced_topics"),
        Path("00_learning/11_mini_projects"),
        Path("00_learning/utils"),
    ]
    create_dirs(learning_dirs)

    print("Creating example project skeleton...")
    proj_root = Path("01_projects/customer_support_bot")
    project_dirs = [
        proj_root / "src/app_streamlit",
        proj_root / "src/app_api",
        proj_root / "src/utils",
        proj_root / "notebooks",
        proj_root / "config",
        proj_root / "data/raw",
        proj_root / "data/processed",
        proj_root / "data/embeddings",
        proj_root / "logs",
        proj_root / "infra/k8s",
        proj_root / "tests",
    ]
    create_dirs(project_dirs)

    project_files = [
        proj_root / "README.md",
        proj_root / "requirements.txt",
        proj_root / ".env.dev_example",
    ]
    create_files(project_files)

    print("Creating src_common utilities placeholders...")
    common_files = [
        Path("src_common/__init__.py"),
        Path("src_common/openai_client.py"),
        Path("src_common/embeddings_client.py"),
        Path("src_common/config_loader.py"),
        Path("src_common/logging_setup.py"),
        Path("src_common/rag_base.py"),
        Path("src_common/file_loader.py"),
        Path("src_common/text_preprocess.py"),
        Path("src_common/eval_utils.py"),
    ]
    create_files(common_files)

    print("Creating config placeholders...")
    write_file(
        Path("config/models.yaml"),
        """
default_model: gpt-4o-mini

models:
  gpt-4o-mini:
    provider: openai
    name: gpt-4o-mini
    max_tokens: 1024
"""
    )

    write_file(
        Path("config/vector_db.yaml"),
        """
default: chroma

chroma:
  persist_directory: ./data/embeddings/dev/
"""
    )

    write_file(
        Path("config/logging.yaml"),
        """
version: 1
disable_existing_loggers: False
"""
    )

    write_file(
        Path("config/app.yaml"),
        "app_name: genai_project"
    )

    print("Creating docs placeholders...")
    write_file(
        Path("docs/environment_setup.md"),
        """
# Environment Setup

- Create virtual environment
- Install dependencies from requirements.txt
- Set APP_ENV=dev|uat|prod and matching .env file in envs/
"""
    )

    write_file(
        Path("docs/architecture_overview.md"),
        """
# Architecture Overview

High-level: User -> LLM -> Vector DB -> Response -> UI
"""
    )

    write_file(
        Path("docs/naming_conventions.md"),
        """
# Naming Conventions

- snake_case for Python files
- lower_snake_case for folders
- UpperCamelCase for classes
"""
    )

    print("Creating top-level files...")
    write_file(
        Path("README.md"),
        """
# genai_project

Central workspace for:
- GenAI learning (LLMs, RAG, agents, UI)
- Real-world GenAI projects
- Dev / UAT / Prod ready architecture
"""
    )

    write_file(
        Path("requirements.txt"),
        "# Core GenAI dependencies will be listed here."
    )

    write_file(
        Path("environment.yml"),
        """
name: genai_env
dependencies:
  - python=3.11
  - pip
  - pip:
      - -r requirements.txt
"""
    )

    write_file(
        Path(".gitignore"),
        """
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
"""
    )

    print("Done! genai_project structure created.")

if __name__ == "__main__":
    main()