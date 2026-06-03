from modules.crud_estudiantes import menu_gestion_estudiantes, ver_cursos_estudiante
from rich.console import Console
from rich.panel import Panel
from rich import box

console = Console()

def mostrar_menu():
    menu = (
        "[bold cyan]1.[/] Gestion de estudiantes\n"
        "[bold cyan]2.[/] Gestion de cursos\n"
        "[bold cyan]3.[/] Gestion de matriculas\n"
        "[bold cyan]4.[/] Ver cursos de un estudiante\n"
        "[bold cyan]5.[/] Ver estudiantes de un curso\n"
        "[bold cyan]6.[/] Ver creditos totales de un estudiante\n"
        "[bold cyan]0.[/] Salir"
    )
    
    console.print(Panel(
        menu, 
        title="[bold cyan]MENU PRINCIPAL[/]", 
        title_align="center",
        box=box.ROUNDED,
        border_style="cyan",
        expand=False
    ))

def main():
    while True:
        mostrar_menu()
        opcion = console.input("\nSeleccione una opcion: ").strip()

        match opcion:
            case "1":
                menu_gestion_estudiantes()

            case "2":
                console.print("[bold blue]Accediendo a Gestion de cursos...[/bold blue]")

            case "3":
                console.print("[bold blue]Accediendo a Gestion de matriculas...[/bold blue]")

            case "4":
                ver_cursos_estudiante()

            case "5":
                console.print("[bold blue]Cargando estudiantes del curso...[/bold blue]")

            case "6":
                console.print("[bold blue]Calculando creditos totales...[/bold blue]")

            case "0":
                console.print("[bold red]Saliendo del sistema...[/bold red]")
                break

            case _:
                console.print("[bold red]Opcion no valida, intente de nuevo.[/bold red]")

if __name__ == "__main__":
    main()