import importlib.util
import os
import sys
from pathlib import Path

from rich.console import Console

console = Console()

current_dir = Path(__file__).resolve().parent
funciones_path = current_dir / "funciones.py"

if funciones_path.exists():
    spec = importlib.util.spec_from_file_location("funciones", str(funciones_path))
    fn = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fn)
else:
    console.print(f"[red]✖ No se encontró el módulo 'funciones' en {funciones_path}[/red]")
    sys.exit(1)


while True:

    console.print("""
[cyan]---------------- MENU ----------------[/cyan]

1. Crear estudiante
2. Mostrar estudiantes
3. Actualizar estudiante
4. Eliminar estudiante

5. Crear curso
6. Mostrar cursos
7. Actualizar curso
8. Eliminar curso

9. Matricular estudiante
10. Ver cursos de un estudiante
11. Ver estudiantes de un curso
12. Total de creditos

13. Salir
""")

    opcion = input("Seleccione una opcion: ")

    match opcion:

        case "1":
            fn.crear_estudiante()

        case "2":
            fn.mostrar_estudiantes()

        case "3":
            fn.actualizar_estudiante()

        case "4":
            fn.eliminar_estudiante()

        case "5":
            fn.crear_curso()

        case "6":
            fn.mostrar_cursos()

        case "7":
            fn.actualizar_curso()

        case "8":
            fn.eliminar_curso()

        case "9":
            fn.matricular_estudiante()

        case "10":
            fn.ver_cursos_estudiante()

        case "11":
            fn.ver_estudiantes_curso()

        case "12":
            fn.total_creditos()

        case "13":
            console.print("[green]✔ Programa finalizado[/green]")
            break

        case _:
            console.print("[red]✖ Opción invalida[/red]")

