# 🏦 NeoBank AI Assistant

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/🦜-LangChain-green)](https://langchain.com/)
[![LangGraph](https://img.shields.io/badge/🔗-LangGraph-orange)](https://langchain-ai.github.io/langgraph/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

> **Projeto educacional** demonstrando a evolução dos workflows de IA: do chatbot simples ao agente autônomo.

## 📖 Sobre o Projeto

O NeoBank AI Assistant é um assistente bancário inteligente que demonstra **3 tipos de workflows de IA**, cada um com diferentes níveis de autonomia e complexidade:

| Workflow           | Descrição                      | Quando Usar                   |
| ------------------ | ------------------------------ | ----------------------------- |
| 🔵 **Non-Agentic** | Pergunta → LLM → Resposta      | FAQs, conceitos, dicas gerais |
| 🟢 **Agentic**     | Usa ferramentas + padrão ReAct | Consultas, análises simples   |
| 🔴 **AI Agent**    | Autônomo com LangGraph         | Planejamento complexo         |

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────────────────────┐
│                        NeoBank AI Assistant                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│    CLI (Rich)  ───►  Workflows  ───►  Tools  ───►  Data Layer       │
│                                                                     │
│       ┌─────────────┐   ┌─────────────┐   ┌─────────────┐           │
│       │ Non-Agentic │   │   Account   │   │   Models    │           │
│       │   Agentic   │   │    Card     │   │  (Pydantic) │           │
│       │  AI Agent   │   │  Analysis   │   │             │           │
│       │ (LangGraph) │   │  Planning   │   │  Mock DB    │           │
│       └─────────────┘   └─────────────┘   └─────────────┘           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## 📂 Estrutura do Projeto

```
neobank-assistant/
├── src/neobank_assistant/     # Pacote principal
│   ├── cli/                   # Interface de comando
│   ├── core/                  # Config + Exceptions
│   ├── data/                  # Models + Mock Database
│   ├── tools/                 # 11 ferramentas LangChain
│   └── workflows/             # 3 tipos de workflow
├── tests/                     # Testes (unit + integration)
├── docs/                      # Documentação + Tutoriais
├── examples/                  # Exemplos de uso
├── scripts/                   # Scripts de automação
└── pyproject.toml            # Configuração (PEP 621)
```

## 🚀 Instalação

### Opção 1: Com Poetry (Recomendado)

```bash
# Clone o repositório
git clone https://github.com/alevtelles/neobank-assistant.git
cd neobank-assistant

# Instale dependências
poetry install

# Configure ambiente
cp .env.example .env
# Edite .env com sua OPENAI_API_KEY

# Execute
poetry run neobank
```

### Opção 2: Com pip

```bash
# Clone o repositório
git clone https://github.com/alevtelles/neobank-assistant.git
cd neobank-assistant

# Crie ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Instale dependências
pip install -e ".[dev]"

# Configure ambiente
cp .env.example .env
# Edite .env com sua OPENAI_API_KEY

# Execute
neobank
```

### Opção 3: Setup Automático

```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
# OpenAI (obrigatório)
OPENAI_API_KEY=sk-sua-chave-aqui
OPENAI_MODEL=gpt-4o-mini
OPENAI_TEMPERATURE=0.1

# Aplicação
APP_ENV=development
LOG_LEVEL=INFO
```

## 🎮 Uso

### Menu Interativo

```bash
# Com Poetry
poetry run neobank

# Com pip (ambiente ativado)
neobank

# Com Make
make run
```

### Programático

```python
from neobank_assistant import NonAgenticAssistant, AgenticAssistant, AIAgentAssistant

# Non-Agentic (simples)
assistant = NonAgenticAssistant()
response = assistant.chat("O que é a regra 50-30-20?")

# Agentic (com ferramentas)
agent = AgenticAssistant()
result = agent.chat("Qual é o saldo da minha conta?")

# AI Agent (autônomo)
ai_agent = AIAgentAssistant()
result = ai_agent.execute("Organize minhas finanças para guardar R$ 5.000 em 6 meses")
```

## 🔧 Ferramentas Disponíveis

| Categoria       | Ferramenta                     | Descrição                        |
| --------------- | ------------------------------ | -------------------------------- |
| 💰 **Account**  | `get_account_balance`          | Consulta saldo por tipo de conta |
|                 | `get_all_balances`             | Visão geral de todas as contas   |
|                 | `get_customer_profile`         | Perfil completo do cliente       |
| 💳 **Card**     | `get_card_info`                | Informações do cartão            |
|                 | `request_limit_increase`       | Solicita aumento de limite       |
| 📊 **Analysis** | `analyze_spending_by_category` | Análise de gastos por categoria  |
|                 | `get_spending_insights`        | Insights e recomendações         |
|                 | `compare_periods`              | Compara gastos entre períodos    |
| 📋 **Planning** | `calculate_savings_plan`       | Plano de poupança                |
|                 | `create_budget_recommendation` | Orçamento 50-30-20               |
|                 | `analyze_financial_health`     | Diagnóstico financeiro           |

## 🧪 Testes

```bash
# Todos os testes
make test

# Com cobertura
make test-cov

# Apenas unitários
make test-unit
```

## 📏 Qualidade de Código

```bash
# Lint
make lint

# Formatar
make format

# Type check
make type-check

# Tudo junto
make check
```

## 📦 Build

```bash
# Gera pacote (wheel + sdist)
make build

# Publica no TestPyPI
make publish-test

# Publica no PyPI
make publish
```

## 📚 Material Didático

O tutorial completo está em `docs/tutorials/modulo-workflows-ia.md` com:

- ✅ Explicação teórica dos 3 tipos de workflow
- ✅ Diagramas de arquitetura
- ✅ Código comentado linha por linha
- ✅ Exercícios práticos
- ✅ Comparativos e trade-offs

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'feat: adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

### Padrão de Commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Documentação
- `refactor:` Refatoração
- `test:` Testes

## 📄 Licença

Este projeto está sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

**Alexsander Valente**

- Website: [alexsander.app.br](https://alexsander.app.br)
- GitHub: [@alevtelles](https://github.com/alevtelles)
- Email: contato@alexsander.app.br

## 🙏 Agradecimentos

- [LangChain](https://langchain.com/) - Framework para LLMs
- [LangGraph](https://langchain-ai.github.io/langgraph/) - Grafos de estado para agentes
- [OpenAI](https://openai.com/) - Modelos de linguagem
- [Pydantic](https://docs.pydantic.dev/) - Validação de dados
- [Rich](https://rich.readthedocs.io/) - Terminal bonito

---

⭐ **Se este projeto te ajudou, deixe uma estrela!**
