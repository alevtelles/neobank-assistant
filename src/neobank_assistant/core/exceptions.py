"""
Exceções Customizadas
=====================
Hierarquia de exceções para tratamento de erros específicos do projeto.

Hierarquia:
    NeoBankError (base)
    ├── ConfigurationError
    ├── ToolExecutionError
    ├── WorkflowError
    │   ├── NonAgenticError
    │   ├── AgenticError
    │   └── AIAgentError
    └── DataError
"""
class NeoBankError(Exception):
    """
    Exceção base para todos os erros do NeoBank Assistant.

    Todas as exceções customizadas devem herdar desta classe
    para facilitar o tratamento centralizado de erros.

    Attributes:
        message: Mensagem de erro
        details: Detalhes adicionais (opcional)
    """

    def __init__(self, message: str, details: dict | None = None) -> None:
        self.message = message
        self.details = details or {}
        super().__init__(self.message)

    
    def __str__(self) -> str:
        if self.details:
            return f"{self.message} | Details: {self.details}"
        return self.message
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.message!r}, details={self.details!r})"
    

class ConfigurationError(NeoBankError):
    """
    Erro de configuração.

    Levantado quando há problemas com variáveis de ambiente,
    arquivos de configuração ou parâmetros inválidos.

    Examples:
        >>> raise ConfigurationError("OPENAI_API_KEY não configurada")
        >>> raise ConfigurationError(
        ...     "Modelo inválido",
        ...     details={"model": "gpt-5", "allowed": ["gpt-4o", "gpt-4o-mini"]}
        ... )
    """

    pass


class ToolExecutionError(NeoBankError):
    """
    Erro na execução de uma ferramenta.

    Levantado quando uma tool do LangChain falha durante execução.

    Attributes:
        tool_name: Nome da ferramenta que falhou
        input_args: Argumentos passados para a ferramenta
    """

    def __init__(
            self,
            message: str,
            tool_name: str | None = None,
            input_args: dict | None = None, 
            details: dict | None = None,
    ) -> None:
        self.tool_name = tool_name,
        self.input_args = input_args,
        super().__init__(
            message,
            details={
                **(details or {}),
                "tool_name": tool_name,
                "input_args": input_args,
            },
        )


class WorkflowError(NeoBankError):
    """
    Erro base para workflows.

    Classe base para erros específicos de cada tipo de workflow.
    """
    pass


class NonAgenticError(WorkflowError):
    """
    Erro no workflow Non-Agentic.

    Levantado quando há falhas no processamento simples
    de pergunta/resposta.
    """

    pass

class AgenticError(WorkflowError): 
    """
    Erro no workflow Agentic.

    Levantado quando há falhas no ciclo ReAct ou
    na execução de ferramentas pelo agente.

    Attributes:
        iteration: Número da iteração em que ocorreu o erro
        last_action: Última ação tentada
    """

    def __init__(
        self,
        message: str,
        iteration: int | None = None,
        last_action: str | None = None, 
        details: dict | None = None,
    ) -> None: 
        self.iteration = iteration,
        self.last_action = last_action,
        super().__init__(
            message,
            details={
                **(details or {}),
                "iteration": iteration,
                "last_action": last_action,
            },
        )

class AIAgentError(WorkflowError):
    """
    Erro no workflow AI Agent.

    Levantado quando há falhas no grafo de estados,
    planejamento ou execução do agente autônomo.

    Attributes:
        current_node: Nó do grafo onde ocorreu o erro
        state
    """

    def __init__(
            self, 
            message: str, 
            current_node: str | None = None,
            state: dict | None = None,
            details: dict | None = None,
        ) -> None:
            self.current_node = current_node,
            self.state = state,
            super().__init__(
                message, 
                details={
                    **(details or{}),
                    "current_node": current_node,
                    "state_keys": list(state.keys()) if state else None,
                },
            )

class DataError(NeoBankError):
     """
    Erro relacionado a dados.

    Levantado quando há problemas com dados do cliente,
    transações ou validação de modelos.

    Attributes:
        model_name: Nome do modelo Pydantic envolvido
        field: Campo que causou o erro
    """
     
     def __init__(
            self, 
            message: str, 
            model_name: str | None = None,
            field: str | None = None,
            details: dict | None = None,
     ) -> None:
        self.model_name = model_name,
        self.field = field,
        super().__init__(
            message,
            details={
                **(details or {}),
                "model_name": model_name,
                "field": field
            },
        )