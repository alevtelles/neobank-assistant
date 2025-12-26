## Os 3 Tipos de Workflows de IA

- Caso Prático: Assistente Bancário Inteligente

#### 📖 O Problema de Negócio

##### Contexto

Você é Engenheiro de IA no NeoBank, um banco digital em crescimento. A equipe de atendimento está sobrecarregada e a diretoria quer implementar um assistente inteligente para ajudar os clientes.

##### O Desafio

Os clientes fazem perguntas como:

- "Qual o limite do meu cartão?"
- "Quero aumentar meu limite"
- "Analise meus gastos do mês e me dê sugestões de economia"
- "Organize minhas finanças e crie um plano para eu guardar R$ 5.000 em 6 meses"

##### Perceba que essas perguntas têm níveis diferentes de complexidade:

| Pergunta                   | Complexidade | Tipo de Resposta        |
| -------------------------- | ------------ | ----------------------- |
| "Qual meu limite?"         | Simples      | Consulta direta         |
| "Quero aumentar limite"    | Média        | Processo com regras     |
| "Analise meus gastos"      | Alta         | Análise + Recomendações |
| "Crie um plano financeiro" | Muito Alta   | Planejamento autônomo   |

##### A Grande Lição

Não existe bala de prata. Cada tipo de workflow é adequado para um nível de complexidade. Usar um AI Agent para responder "qual meu saldo?" é como usar um canhão para matar uma mosca — funciona, mas é desperdício de recursos.

### 🏗️ Arquitetura Base do Projeto

Antes de implementar os workflows, vamos criar a infraestrutura comum que todos usarão.

#### Estrutura de Pastas

```bash
neobank-assistant/
│
├── config/
│ └── settings.py # Configurações e variáveis de ambiente
│
├── data/
│ └── mock_database.py # Dados simulados do cliente
│
├── tools/
│ ├── **init**.py
│ ├── account_tools.py # Ferramentas de conta
│ ├── card_tools.py # Ferramentas de cartão
│ ├── analysis_tools.py # Ferramentas de análise
│ └── planning_tools.py # Ferramentas de planejamento
│
├── workflows/
│ ├── **init**.py
│ ├── non_agentic.py # Implementação Non-Agentic
│ ├── agentic.py # Implementação Agentic Workflow
│ └── ai_agent.py # Implementação AI Agent
│
├── main.py # Ponto de entrada
└── requirements.txt # Dependências
```

### 📦 Parte 1: Preparação do Ambiente

#### 1.1 Dependências do Projeto

```bash
# requirements.txt

# Framework principal para LLMs
langchain==0.2.16
langchain-openai==0.1.25
langchain-community==0.2.16

# Framework para agentes com grafos de estado
langgraph==0.2.28

# Utilitários
python-dotenv==1.0.1
pydantic==2.9.2
rich==13.8.1  # Para output bonito no terminal
```

##### Por que cada dependência?

- <code style="background-color:#f3f4f6; color:#b91c1c; padding:2px 6px; border-radius:6px;">langchain</code> : Framework que padroniza a interação com LLMs e fornece abstrações para chains, tools e agents
- <code style="background-color:#f3f4f6; color:#b91c1c; padding:2px 6px; border-radius:6px;">langchain-openai</code> : Integração específica com modelos da OpenAI
- <code style="background-color:#f3f4f6; color:#b91c1c; padding:2px 6px; border-radius:6px;">langGraph</code> : Extensão do LangChain para criar workflows como grafos de estado (essencial para AI Agents)
- <code style="background-color:#f3f4f6; color:#b91c1c; padding:2px 6px; border-radius:6px;">python-dotenv </code>: Carrega variáveis de ambiente de arquivos .env (segurança para API keys)
- <code style="background-color:#f3f4f6; color:#b91c1c; padding:2px 6px; border-radius:6px;">pydantic </code>: Validação de dados com tipos (usado internamente pelo LangChain)
- <code style="background-color:#f3f4f6; color:#b91c1c; padding:2px 6px; border-radius:6px;">rich</code>: Biblioteca para output formatado no terminal (facilita debug e demonstrações)
