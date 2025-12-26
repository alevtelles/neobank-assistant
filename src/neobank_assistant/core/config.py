"""
Configuração Centralizada
=========================

Gerencia todas as configuraçõees do projeto usando Pydantic Settings.
Carrga automaticamente variáveis de ambiente e arquivos .env.

Uso:
    from neobank_assistant.core.config import get_settings
    settings = get_settings()
    print(settings.openai_model)

"""

from functools import lru_cache     # Cache para singleton
from typing import Literal          # Tipos literais

from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
        Configuração da aplicação.

        Valores são carregados na seguinte ordem de prioridade:
        1. Variáveis de ambiente
        2. Arquivo .env
        3. Valores padrão definidos aqui

        Attributes:
            openai_api_key: Chave de API da OpenAI (Obrigatório).
            openai_model: Modelo da OpenAI a ser utilizado.
            openai_temperature: Temperatura para geração.
            openai_max_tokens: Máximo de tokens para resposta.
            app_env: Ambiente da aplicação.
            log_level: Nível de logging.
    """

    model_config = SettingsConfigDict(
            env_file=".env",
            env_file_encoding="utf-8",
            case_sensitive=False,
            extra="ignore",
        )
    
    # =============== OPENAI CONFIG ===============
    openai_api_key: SecretStr = Field(
        ..., # Obrigatório
        description="Chave de API da OpenAI",
    )

    openai_model: str = Field(
        default="gpt-4o-mini",
        description="Modelo da OpenAI a ser usado",
    )

    openai_temperature: float = Field(
        default=0.1,
        ge=0.0,
        le=2.0,
        description="Temperatuda para geração (0.0-2.0)",
    )

    openai_max_tokens: int = Field(
        default=2000,
        ge=1,
        le=128000,
        description="Máximo de tokens na Resposta",
    )

    # ============== LangChain / LangSmith ==================

    langchain_tracing_v2: bool = Field(
        default=False,
        description="Habilitar tracing do LangSmith",
    )

    langchain_api_key: SecretStr | None = Field(
        default=None,
        description="Chave de API do LangSmith",
    )

    langchain_project: str = Field(
        default="neobank-assistant",
        description="Nome do Projeto no LangSmith",
    )


    # ============== Application  ==================
    app_env: Literal["development", "staging", "production"] = Field(
        default="development",
        description="Ambiente da aplicação",
    )

    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROS"] = Field(
        default="INFO",
        description="Nivel de logging",
    )

     # ============== Azure OpenAI (Opicional meu querido!!)  ==================

    azure_openai_endpoint: str | None = Field(
        default=None,
        description="Endpoint do Azure OpenAI",
     )
    
    azure_openai_api_key: SecretStr | None = Field(
        default=None,
        description="Chave da API Azure OPENAI",
    )

    azure_openai_deployment: str | None = Field (
        default=None,
        description="Nome do deployment no Azure"
    )

    azure_openai_api_version: str = Field(
        default="2025-12-26",
        description="Versão da API do Azure OpenAI"
    )

     # ============== Validators  ==================

    @field_validator("openai_model")
    @classmethod
    def validate_model(cls, v: str) -> str:
        """ Valida se o modelo é suportado ."""
        allwed_models =[
            "gpt-4o",
            "gpt-4o-mini",
            "gpt-4-turbo",
            "gpt-4",
            "gpt-3.5-turbo",
        ]

        if v not in allwed_models:
            # permite modelos custom (Azure, fine-tuned, etc)
            pass

        return v
    
       # ============== Properties  ==================

    @property
    def is_production(self) -> bool:
        """Verifica se está em ambiente de produção """
        return self.app_env == "production"
    
    @property
    def is_development(self) -> bool:
        """Verifica se esta em ambiente de desenvolvimento"""
        return self.app_env == "development"
    
    @property
    def use_azure(self) -> bool:
        """Verifica se deve usar Azure OpenAI"""
        return (
            self.azure_openai_endpoint is not None
            and self.azure_openai_api_key is not None
            and self.azure_openai_deployment is not None
        )
    
    @property
    def langsmith_enabled(self) -> bool:
        """Verifica se LangSmith está habilitado"""
        return self.langchain_tracing_v2 and self.langchain_api_key is not None
    

       # ============== Methods  ==================
    def get_llm_kwargs(self) -> dict:
        """
            Retorna kwargs para inicializar o LLM.

            Returns:
                Dicionário com configurações do modelo
        
        """
        
        if self.use_azure:
            assert self.azure_openai_api_key is not None
            return {
            "azure_endpoint": self.azure_openai_endpoint,
            "api_key": self.azure_openai_api_key.get_secret_value(),
            "azure_deployment": self.azure_openai_deployment,
            "api_version": self.azure_openai_api_version,
            "temperature": self.openai_temperature,  # typo: era "temparature"
            "max_tokens": self.openai_max_tokens
        }
        
        return {
            "api_key": self.openai_api_key.get_secret_value(),
            "model": self.openai_model,
            "temperature": self.openai_temperature,
            "max_tokens": self.openai_max_tokens
        }
    
    def __repr__(self) -> str:
        """Representação segura (sem expor secrets)"""
        return(
            f"Settings("
            f"model={self.openai_model!r}, "
            f"env={self.app_env!r}, "
            f"azure={self.use_azure}, "
            f"langsmith={self.langsmith_enabled}"
            f")"
        )
    
@lru_cache
def get_settings() -> Settings:
    """
        Retonra instância singleton das configurações

        Usa cache para evitar recarrgar o .env múltiplas vezes.

        Returns:
            Instância de Setttings

        Raises:
            ValidationError: Se configurações obrigatórias estiverem faltando
    """

    return Settings() # type: ignore[call-arg]