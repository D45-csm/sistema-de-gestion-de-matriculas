import json
from rich.console import Console
from rich.table import Table
console = Console()

def cargar_datos():

    try:
        with open("datos_entidades.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
        
    except FileNotFoundError:
        return {
            "estudiantes": [],
            "cursos": [],
            "matriculas": []
        }

def guardar_datos(datos):

    try:
        with open("datos_entidades.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4)
        console.print("[green]✔ Datos guardados correctamente[/green]")
    except Exception:
        console.print("[red]✖ Ocurrio un error al guardar los datos[/red]")

# CRUD ESTUDIANTES

# Crear estudiante
def crear_estudiante():

    datos = cargar_datos()
    try:
        nombre = input("Nombre: ")
        carrera = input("Carrera: ")
        if nombre == "" or carrera == "":
            console.print("[yellow]⚠ Todos los campos son obligatorios[/yellow]")
            return
        datos["estudiantes"].append({
            "id_estudiante": len(datos["estudiantes"]) + 1,
            "nombre": nombre,
            "carrera": carrera
        })
        guardar_datos(datos)
        console.print("[green]✔ Estudiante creado correctamente[/green]")
    except ValueError:
        console.print("[red]✖ Error en los datos ingresados[/red]")

# Mostrar estudiantes
def mostrar_estudiantes():

    datos = cargar_datos()
    estudiantes = datos["estudiantes"]
    if len(estudiantes) == 0:
        console.print("[yellow]No hay estudiantes registrados[/yellow]")
        return
    table = Table(title="Lista de Estudiantes")
    table.add_column("ID")
    table.add_column("Nombre")
    table.add_column("Carrera")

    for estudiante in estudiantes:
        table.add_row(
            str(estudiante["id_estudiante"]),
            estudiante["nombre"],
            estudiante["carrera"]
        )
    console.print(table)

# Actualizar estudiante
def actualizar_estudiante():

    datos = cargar_datos()
    try:
        id_estudiante = int(input("Ingrese ID estudiante: "))
        for estudiante in datos["estudiantes"]:
            if estudiante["id_estudiante"] == id_estudiante:
                estudiante["nombre"] = input("Nuevo nombre: ")
                estudiante["carrera"] = input("Nueva carrera: ")
                guardar_datos(datos)
                console.print("[green]✔ Estudiante actualizado correctamente[/green]")
                return
        console.print("[yellow]⚠ Estudiante no encontrado[/yellow]")
    except ValueError:
        console.print("[red]✖ ID invalido[/red]")

# Eliminar estudiante
def eliminar_estudiante():

    datos = cargar_datos()
    try:
        id_estudiante = int(input("Ingrese ID estudiante: "))
        for estudiante in datos["estudiantes"]:
            if estudiante["id_estudiante"] == id_estudiante:
                datos["estudiantes"].remove(estudiante)
                guardar_datos(datos)
                console.print("[green]✔ Estudiante eliminado correctamente[/green]")
                return
        console.print("[yellow]⚠ Estudiante no encontrado[/yellow]")
    except ValueError:
        console.print("[red]✖ ID invalido[/red]")

# CRUD CURSOS

# Crear curso
def crear_curso():

    datos = cargar_datos()
    try:
        id_curso = int(input("ID del curso: "))
        nombre_curso = input("Nombre del curso: ")
        creditos = int(input("Creditos: "))
        datos["cursos"].append({
            "id_curso": id_curso,
            "nombre_curso": nombre_curso,
            "creditos": creditos
        })
        guardar_datos(datos)
        console.print("[green]✔ Curso creado correctamente[/green]")
    except ValueError:
        console.print("[red]✖ Datos invalidos[/red]")

# Mostrar cursos
def mostrar_cursos():

    datos = cargar_datos()
    cursos = datos["cursos"]
    if len(cursos) == 0:
        console.print("[yellow]No hay cursos registrados[/yellow]")
        return
    table = Table(title="Lista de Cursos")
    table.add_column("ID")
    table.add_column("Nombre")
    table.add_column("Creditos")
    for curso in cursos:
        table.add_row(
            str(curso["id_curso"]),
            curso["nombre_curso"],
            str(curso["creditos"])
        )
    console.print(table)

# Actualizar curso
def actualizar_curso():

    datos = cargar_datos()
    try:
        id_curso = int(input("Ingrese ID del curso: "))
        for curso in datos["cursos"]:
            if curso["id_curso"] == id_curso:
                curso["nombre_curso"] = input("Nuevo nombre: ")
                curso["creditos"] = int(input("Nuevos creditos: "))
                guardar_datos(datos)
                console.print("[green]✔ Curso actualizado correctamente[/green]")
                return
        console.print("[yellow]⚠ Curso no encontrado[/yellow]")
    except ValueError:
        console.print("[red]✖ ID invalido[/red]")

# Eliminar curso
def eliminar_curso():

    datos = cargar_datos()
    try:
        id_curso = int(input("Ingrese ID del curso: "))
        for curso in datos["cursos"]:
            if curso["id_curso"] == id_curso:
                datos["cursos"].remove(curso)
                guardar_datos(datos)
                console.print("[green]✔ Curso eliminado correctamente[/green]")
                return
        console.print("[yellow]⚠ Curso no encontrado[/yellow]")
    except ValueError:
        console.print("[red]✖ ID invalido[/red]")

# MATRICULAR ESTUDIANTE
def matricular_estudiante():

    datos = cargar_datos()
    try:
        id_estudiante = int(input("Ingrese ID del estudiante: "))
        cantidad = int(input("Cantidad de cursos a matricular: "))
        lista_cursos = []
        for numero in range(cantidad):
            id_curso = int(input("Ingrese ID del curso: "))
            lista_cursos.append(id_curso)
        periodo = input("Periodo académico: ")
        datos["matriculas"].append({
            "id_matricula": len(datos["matriculas"]) + 1,
            "id_estudiante": id_estudiante,
            "id_curso": lista_cursos,
            "periodo_academico": periodo
        })
        guardar_datos(datos)
        console.print("[green]✔ Matrícula registrada correctamente[/green]")
    except ValueError:
        console.print("[red]✖ Datos invalidos[/red]")

# VER CURSOS DE UN ESTUDIANTE
def ver_cursos_estudiante():

    datos = cargar_datos()
    id_estudiante = int(input("Ingrese ID del estudiante: "))
    encontrado = False
    for matricula in datos["matriculas"]:
        if matricula["id_estudiante"] == id_estudiante:
            encontrado = True
            table = Table(title="Cursos del Estudiante")
            table.add_column("Cursos")
            for curso in datos["cursos"]:
                if curso["id_curso"] in matricula["id_curso"]:
                    table.add_row(curso["nombre_curso"])
            console.print(table)
    if not encontrado:
        console.print("[yellow]⚠ El estudiante no tiene cursos matriculados[/yellow]")

# VER ESTUDIANTES DE UN CURSO
def ver_estudiantes_curso():

    datos = cargar_datos()
    try:
        id_curso = int(input("Ingrese ID del curso: "))
        encontrado = False
        table = Table(title="Estudiantes del Curso")
        table.add_column("Nombre")
        for matricula in datos["matriculas"]:
            if id_curso in matricula["id_curso"]:
                for estudiante in datos["estudiantes"]:
                    if estudiante["id_estudiante"] == matricula["id_estudiante"]:
                        encontrado = True
                        table.add_row(estudiante["nombre"])
        if encontrado:
            console.print(table)
        else:
            console.print("[yellow]⚠ No hay estudiantes en este curso[/yellow]")
    except ValueError:
        console.print("[red]✖ ID invalido[/red]")

# RETO FINAL
# TOTAL DE CRÉDITOS
def total_creditos():

    datos = cargar_datos()
    try:
        id_estudiante = int(input("Ingrese ID del estudiante: "))
        total = 0
        for matricula in datos["matriculas"]:
            if matricula["id_estudiante"] == id_estudiante:
                for id_curso in matricula["id_curso"]:
                    for curso in datos["cursos"]:
                        if curso["id_curso"] == id_curso:
                            total += curso["creditos"]
        console.print(f"[green]✔ Total de creditos: {total}[/green]")
    except ValueError:
        console.print("[red]✖ ID inválido[/red]")