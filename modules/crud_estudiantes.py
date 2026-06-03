from rich.console import Console
from rich.table import Table, box
from rich.panel import Panel
from modules.guardar_cargar_datos import cargar_datos, guardar_datos

console = Console()

def crear_estudiante():
    datos = cargar_datos("data/estudiantes.json")
    
    console.print(Panel("[bold cyan]📝 Registrar Nuevo Estudiante[/bold cyan]", border_style="cyan"))

    while True:
        nombre = input("Ingrese el nombre: ").strip()
        if nombre == "":
            console.print("[bold red]✖ El nombre no puede estar vacio.[/bold red]")
            continue
        repetido = False
        for estudiante in datos:
            if estudiante["nombre"].lower() == nombre.lower():
                repetido = True
                break
        if repetido == True:
            console.print("[bold red]✖ Ese estudiante ya existe.[/bold red]")
        else:
            break

    while True:
        carrera = input("Ingrese la carrera: ").strip()
        if carrera == "":
            console.print("[bold red]✖ La carrera no puede estar vacia.[/bold red]")
        else:
            break

    nuevo_id = 1
    for estudiante in datos:
        if estudiante["id_estudiante"] >= nuevo_id:
            nuevo_id = estudiante["id_estudiante"] + 1

    nuevo_estudiante = {
        "id_estudiante": nuevo_id,
        "nombre": nombre,
        "carrera": carrera
    }

    datos.append(nuevo_estudiante)
    guardar_datos("data/estudiantes.json", datos)

    console.print("[bold green]✔ Estudiante creado correctamente.[/bold green]")


def mostrar_estudiantes():
    datos = cargar_datos("data/estudiantes.json")

    if len(datos) == 0:
        console.print(Panel("[bold yellow]⚠ No hay estudiantes registrados.[/bold yellow]", border_style="yellow"))
        return

    tabla = Table(
        title="🎓 LISTA DE ESTUDIANTES REGISTRADOS", 
        title_style="bold magenta", 
        box=box.ROUNDED
    )

    tabla.add_column("ID", style="cyan", justify="center", width=6)
    tabla.add_column("Nombre")
    tabla.add_column("Carrera")

    for estudiante in datos:
        tabla.add_row(
            str(estudiante["id_estudiante"]),
            estudiante["nombre"],
            estudiante["carrera"]
        )
    
    console.print("\n")
    console.print(tabla)
    console.print("\n")


def actualizar_estudiante():
    datos = cargar_datos("data/estudiantes.json")

    console.print(Panel("[bold yellow]🔄 Actualizar Informacion de Estudiante[/bold yellow]", border_style="yellow"))
    mostrar_estudiantes()

    try:
        id_buscar = int(input("Ingrese el ID a actualizar: "))
    except ValueError:
        console.print("[bold red]✖ Debe ingresar un numero.[/bold red]")
        return

    for estudiante in datos:
        if estudiante["id_estudiante"] == id_buscar:
            nombre = input("Nuevo nombre: ").strip()
            carrera = input("Nueva carrera: ").strip()
            
            if nombre != "":
                estudiante["nombre"] = nombre
            if carrera != "":
                estudiante["carrera"] = carrera
                
            guardar_datos("data/estudiantes.json", datos)

            console.print("[bold green]✔ Estudiante actualizado.[/bold green]")
            return
            
    console.print("[bold red]✖ ID no encontrado.[/bold red]")


def eliminar_estudiante():
    datos = cargar_datos("data/estudiantes.json")

    console.print(Panel("[bold red]❌ Eliminar Registro de Estudiante[/bold red]", border_style="red"))
    mostrar_estudiantes()
    
    try:
        id_buscar = int(input("Ingrese el ID a eliminar: "))
    except ValueError:
        console.print("[bold red]✖ Debe ingresar un numero.[/bold red]")
        return
        
    for estudiante in datos:
        if estudiante["id_estudiante"] == id_buscar:
            datos.remove(estudiante)
            guardar_datos("data/estudiantes.json", datos)
            console.print("[bold green]✔ Estudiante eliminado.[/bold green]")
            return
            
    console.print("[bold red]✖ ID no encontrado.[/bold red]")


def ver_cursos_estudiante():
    console.print(Panel("[bold magenta]🔍 Cursos Matriculados por Estudiante[/bold magenta]", border_style="magenta"))
    mostrar_estudiantes()

    estudiantes = cargar_datos("data/estudiantes.json")
    cursos = cargar_datos("data/cursos.json")
    matriculas = cargar_datos("data/matriculas.json")
    
    while True:
        try:
            id_estudiante = int(input("Ingrese el ID del estudiante para ver sus cursos: "))
        except ValueError:
            console.print("[bold red]✖ Debe ingresar un numero.[/bold red]")
            continue
            
        existe_estudiante = False
        for estudiante in estudiantes:
            if estudiante["id_estudiante"] == id_estudiante:
                existe_estudiante = True
                break

        if existe_estudiante:
            break
        console.print("[bold red]✖ El ID de estudiante no existe. Intente de nuevo.[/bold red]")

    encontrado = False

    for matricula in matriculas:
        if matricula["id_estudiante"] == id_estudiante:
            encontrado = True
            
            table = Table(
                title=f"📚 Cursos Matriculados - Periodo {matricula['periodo_academico']}",
                title_style="bold cyan",
                box=box.ROUNDED,
                header_style="bold white on violet"
            )
            table.add_column("ID Curso", style="cyan", justify="center")
            table.add_column("Nombre Curso", style="green")
            table.add_column("Creditos", style="yellow", justify="center")

            for id_curso_individual in matricula["id_curso"]:
                for curso in cursos:
                    if curso["id_curso"] == id_curso_individual:
                        table.add_row(
                            str(curso["id_curso"]),
                            curso["nombre_curso"],
                            str(curso["creditos"])
                        )
            console.print("\n")
            console.print(table)
            console.print("\n")
            
    if not encontrado:
        console.print(Panel("[bold yellow]⚠ El estudiante no tiene matriculas registradas.[/bold yellow]", border_style="yellow"))


def menu_gestion_estudiantes():
    while True:
        menu_texto = (
            "[bold cyan]1.[/bold cyan] Crear estudiante\n"
            "[bold cyan]2.[/bold cyan] Ver lista de estudiantes\n"
            "[bold cyan]3.[/bold cyan] Actualizar estudiante\n"
            "[bold cyan]4.[/bold cyan] Eliminar estudiante\n"
            "[bold cyan]5.[/bold cyan] Ver cursos de un estudiante\n"
            "[bold cyan]6.[/bold cyan] Volver al menu principal"
        )
        
        console.print("\n")
        console.print(Panel(menu_texto, title="[bold cyan]💼 GESTION DE ESTUDIANTES[/bold cyan]", border_style="cyan", width=45))
        
        opcion = input("\nSeleccione una opcion: ").strip()
        
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
                ver_cursos_estudiante()
            case "6":
                break
            case _:
                console.print("[bold red]Opcion no valida.[/bold red]")