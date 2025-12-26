# ============================================================
# NEOBANK AI ASSISTANT - Makefile
# ============================================================
# Compatível com Poetry (env) + Hatchling (build) + pip
#
# USO:
#   make help       - Lista comandos
#   make install    - Instala com Poetry
#   make install-pip - Instala com pip
#   make run        - Executa o assistente
# ============================================================

.PHONY: help install install-pip install-dev clean test lint format run demo build

# Detecta se Poetry está disponível
POETRY := $(shell command -v poetry 2> /dev/null)

ifdef POETRY
    RUN := poetry run
    INSTALL_CMD := poetry install
else
    RUN :=
    INSTALL_CMD := pip install -e .
endif

# Variáveis
PROJECT := neobank_assistant
SRC_DIR := src/$(PROJECT)
TEST_DIR := tests

# Cores
BLUE := \033[34m
GREEN := \033[32m
YELLOW := \033[33m
RED := \033[31m
NC := \033[0m

# ============================================================
# HELP
# ============================================================
help: ## Mostra esta mensagem de ajuda
	@echo ""
	@echo "$(BLUE)╔══════════════════════════════════════════════════════════╗$(NC)"
	@echo "$(BLUE)║          NeoBank AI Assistant - Comandos Make            ║$(NC)"
	@echo "$(BLUE)╚══════════════════════════════════════════════════════════╝$(NC)"
	@echo ""
ifdef POETRY
	@echo "$(GREEN)✓ Poetry detectado - usando Poetry$(NC)"
else
	@echo "$(YELLOW)⚠ Poetry não detectado - usando pip$(NC)"
endif
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'
	@echo ""

# ============================================================
# INSTALAÇÃO
# ============================================================
install: ## Instala dependências (detecta Poetry/pip)
	@echo "$(BLUE)📦 Instalando dependências...$(NC)"
ifdef POETRY
	poetry install
else
	pip install -e .
endif
	@echo "$(GREEN)✅ Instalação concluída!$(NC)"

install-pip: ## Instala com pip (força pip)
	@echo "$(BLUE)📦 Instalando com pip...$(NC)"
	pip install -e .
	@echo "$(GREEN)✅ Instalação concluída!$(NC)"

install-dev: ## Instala dependências de desenvolvimento
	@echo "$(BLUE)📦 Instalando dependências de desenvolvimento...$(NC)"
ifdef POETRY
	poetry install
	poetry run pre-commit install || true
else
	pip install -e ".[dev]"
	pre-commit install || true
endif
	@echo "$(GREEN)✅ Ambiente de desenvolvimento configurado!$(NC)"

install-all: ## Instala todas as dependências (dev + docs + notebooks)
	@echo "$(BLUE)📦 Instalando todas as dependências...$(NC)"
ifdef POETRY
	poetry install --all-extras
	poetry run pre-commit install || true
else
	pip install -e ".[all]"
	pre-commit install || true
endif
	@echo "$(GREEN)✅ Instalação completa!$(NC)"

# ============================================================
# LIMPEZA
# ============================================================
clean: ## Remove arquivos gerados e caches
	@echo "$(YELLOW)🧹 Limpando arquivos temporários...$(NC)"
	rm -rf build/ dist/ *.egg-info/
	rm -rf .pytest_cache/ .mypy_cache/ .ruff_cache/
	rm -rf .coverage htmlcov/
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	@echo "$(GREEN)✅ Limpeza concluída!$(NC)"

# ============================================================
# TESTES
# ============================================================
test: ## Executa todos os testes
	@echo "$(BLUE)🧪 Executando testes...$(NC)"
	$(RUN) pytest $(TEST_DIR) -v

test-unit: ## Executa apenas testes unitários
	@echo "$(BLUE)🧪 Executando testes unitários...$(NC)"
	$(RUN) pytest $(TEST_DIR)/unit -v -m unit

test-integration: ## Executa testes de integração
	@echo "$(BLUE)🧪 Executando testes de integração...$(NC)"
	$(RUN) pytest $(TEST_DIR)/integration -v -m integration

test-cov: ## Executa testes com cobertura
	@echo "$(BLUE)🧪 Executando testes com cobertura...$(NC)"
	$(RUN) pytest $(TEST_DIR) --cov=$(SRC_DIR) --cov-report=html --cov-report=term-missing
	@echo "$(GREEN)📊 Relatório em htmlcov/index.html$(NC)"

# ============================================================
# QUALIDADE DE CÓDIGO
# ============================================================
lint: ## Verifica estilo de código
	@echo "$(BLUE)🔍 Verificando código...$(NC)"
	$(RUN) ruff check $(SRC_DIR) $(TEST_DIR)

format: ## Formata código
	@echo "$(BLUE)✨ Formatando código...$(NC)"
	$(RUN) ruff format $(SRC_DIR) $(TEST_DIR)
	$(RUN) ruff check --fix $(SRC_DIR) $(TEST_DIR)
	@echo "$(GREEN)✅ Código formatado!$(NC)"

type-check: ## Verifica tipos com MyPy
	@echo "$(BLUE)🔎 Verificando tipos...$(NC)"
	$(RUN) mypy $(SRC_DIR)

check: lint type-check ## Todas as verificações
	@echo "$(GREEN)✅ Verificações OK!$(NC)"

# ============================================================
# EXECUÇÃO
# ============================================================
run: ## Executa o assistente (menu interativo)
	@echo "$(BLUE)🚀 Iniciando NeoBank AI Assistant...$(NC)"
	$(RUN) neobank

demo: ## Executa demonstração rápida
	@echo "$(BLUE)🎬 Executando demonstração...$(NC)"
	$(RUN) python examples/basic_usage.py

shell: ## Abre shell Python interativo
	@echo "$(BLUE)🐍 Abrindo shell...$(NC)"
	$(RUN) ipython

# ============================================================
# BUILD & PUBLISH
# ============================================================
build: clean ## Gera pacote para distribuição
	@echo "$(BLUE)📦 Gerando pacote com Hatch...$(NC)"
	pip install build
	python -m build
	@echo "$(GREEN)✅ Pacote gerado em dist/$(NC)"

publish-test: build ## Publica no TestPyPI
	@echo "$(BLUE)🚀 Publicando no TestPyPI...$(NC)"
	pip install twine
	python -m twine upload --repository testpypi dist/*

publish: build ## Publica no PyPI (produção)
	@echo "$(RED)⚠️  Publicando no PyPI de PRODUÇÃO!$(NC)"
	@read -p "Tem certeza? [y/N] " confirm && [ "$$confirm" = "y" ]
	pip install twine
	python -m twine upload dist/*

# ============================================================
# DOCUMENTAÇÃO
# ============================================================
docs: ## Gera documentação
	@echo "$(BLUE)📚 Gerando documentação...$(NC)"
	$(RUN) mkdocs build
	@echo "$(GREEN)✅ Documentação em site/$(NC)"

serve-docs: ## Serve documentação localmente
	@echo "$(BLUE)📚 Servindo docs em http://localhost:8000$(NC)"
	$(RUN) mkdocs serve

# ============================================================
# SETUP INICIAL
# ============================================================
setup: ## Configuração inicial completa
	@echo "$(BLUE)🔧 Configurando projeto...$(NC)"
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "$(YELLOW)⚠️  Arquivo .env criado. Configure sua OPENAI_API_KEY!$(NC)"; \
	fi
	@make install-dev
	@echo ""
	@echo "$(GREEN)╔══════════════════════════════════════════════════════════╗$(NC)"
	@echo "$(GREEN)║              ✅ Setup concluído com sucesso!             ║$(NC)"
	@echo "$(GREEN)╠══════════════════════════════════════════════════════════╣$(NC)"
	@echo "$(GREEN)║  Próximos passos:                                        ║$(NC)"
	@echo "$(GREEN)║  1. Edite .env com sua OPENAI_API_KEY                    ║$(NC)"
	@echo "$(GREEN)║  2. Execute: make run                                    ║$(NC)"
	@echo "$(GREEN)╚══════════════════════════════════════════════════════════╝$(NC)"