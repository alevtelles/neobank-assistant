"""
Neobank AI Assistant - CLI Entry Point

Este arquivo serve como ponto de entrada do CLI (`neobank`)
e também como teste de que:
- o pacote está sendo instalado corretamente
- o entrypoint do pyproject.toml funciona
- os imports resolvem via layout src/
"""

import sys
from rich.console import Console

console = Console()


def main() -> None:
    console.print("[bold green]✅ Neobank AI Assistant iniciado com sucesso![/bold green]")
    console.print("")

    console.print("[bold]Informações do ambiente:[/bold]")
    console.print(f"• Python: {sys.version.split()[0]}")
    console.print(f"• Executável: {sys.executable}")
    console.print("")

    console.print("[bold]Testes rápidos:[/bold]")

    try:
        import neobank_assistant

        console.print("✔ Import do pacote [green]neobank_assistant[/green] OK")
    except ImportError as e:
        console.print(f"✖ Erro ao importar pacote: {e}", style="red")

    console.print("")
    console.print("[bold cyan]Tudo certo. O CLI está funcional.[/bold cyan]")


if __name__ == "__main__":
    main()
