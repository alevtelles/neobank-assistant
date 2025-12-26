"""
NeoBanck AI Assistant
=====================
Assistente bancário inteligente demonstrando 3 tipos de workflows de IA.
"""

# Versão do pacote (usada pelo pip e setuptools)
__version__ = "0.1.0"

# Imports públicos - o que os usuários podem importar diretamente.
from neobank_assistant.workflows import(
    NonAgenticAssistant,    # Workflow simples
    AgenticAssistant,       # Workflow com ferramentas
    AIAgentAssistante       # Agente autônomo
)

# Define explicitamente o que é exportado
__all__ = [
    "__version__",
    "NonAgenticAssistant",
    "AgenticAssistant",
    "AIAgentAssistante"
]

# Isso permite:
# from neobank_assistant import NonAgenticAssistant
# from neobank_assistant import __version__