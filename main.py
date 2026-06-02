# import funciones as fn
from funciones import *
from rich.console import Console

console = Console()


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
            crear_estudiante()

        case "2":
            mostrar_estudiantes()

        case "3":
            actualizar_estudiante()

        case "4":
            eliminar_estudiante()

        case "5":
            crear_curso()

        case "6":
            mostrar_cursos()

        case "7":
            actualizar_curso()

        case "8":
            eliminar_curso()

        case "9":
            matricular_estudiante()

        case "10":
            ver_cursos_estudiante()

        case "11":
            ver_estudiantes_curso()

        case "12":
            total_creditos()

        case "13":
            console.print("[green]✔ Programa finalizado[/green]")
            break

        case _:
            console.print("[red]✖ Opción invalida[/red]")

