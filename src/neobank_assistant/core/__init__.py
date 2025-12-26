"""
Core module
===========
Configurações centrais e exceções do projeto.

"""

from neobanck_assistant.core.config import Settings, get_settings
from neobanck_assistant.core.exceptions import (
    AgenticError,
    AIAgentError,
    ConfigurationError,
    DataError,
    NeoBanckError,
    NonAgenticError,
    ToolExecutionError,
    WorkflowError,
)

__all__ = [
    "Settings",
    "get_settings",
    "NeoBanckError",
    "ConfigurationError",
    "ToolExecutionError",
    "WorkflowError",
    "NonAgenticError",
    "AgenticError",
    "AIAgentError",
    "DataError",
]