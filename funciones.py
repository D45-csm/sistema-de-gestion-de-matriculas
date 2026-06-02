import json
import sys
from entidades_principales import  *
from guardar_cargar_datos import cargar_datos, guardar_datos
from rich.console import Console
from rich.table import Table
console = Console()

# --- VALIDACIONES LOCALES ---

def pedir_texto(mensaje):
    """Insiste localmente si el campo está vacío. Escribir 'salir' cierra el programa."""
    while True:
        valor = input(f"{mensaje} o digite 'salir' para finalizar: ").strip()
        if valor.lower() == 'salir':
            console.print("[green]✔ Programa finalizado por el usuario.[/green]")
            sys.exit()
        if valor == "":
            console.print("[yellow]⚠ Todos los campos son obligatorios. Intente de nuevo.[/yellow]")
            continue
        return valor

def pedir_entero(mensaje):
    """Insiste si no es un número entero. Escribir 'salir' cierra el programa."""
    while True:
        valor = input(f"{mensaje} o digite 'salir' para finalizar: ").strip()
        if valor.lower() == 'salir':
            console.print("[green]✔ Programa finalizado por el usuario.[/green]")
            sys.exit()
        if valor == "":
            console.print("[yellow]⚠ Este campo es obligatorio. Intente de nuevo.[/yellow]")
            continue
        try:
            return int(valor)
        except ValueError:
            console.print("[red]✖ Error: Debe ingresar un número entero válido.[/red]")


# --- CRUD ESTUDIANTES ---

def crear_estudiante():
    datos = cargar_datos()
    nombre = pedir_texto("Ingrese el nombre del estudiante")
    carrera = pedir_texto("Ingrese la carrera del estudiante")
    
    nuevo_id = 1
    for estudiante in datos["estudiantes"]:
        if estudiante["id_estudiante"] >= nuevo_id:
            nuevo_id = estudiante["id_estudiante"] + 1

    datos["estudiantes"].append({
        "id_estudiante": nuevo_id,
        "nombre": nombre,
        "carrera": carrera
    })
    guardar_datos(datos)
    console.print(f"[green]✔ Estudiante creado con ID: {nuevo_id}[/green]")

def mostrar_estudiantes():
    datos = cargar_datos()
    if not datos["estudiantes"]:
        console.print("[yellow]No hay estudiantes registrados[/yellow]")
        return
    table = Table(title="Lista de Estudiantes")
    table.add_column("ID")
    table.add_column("Nombre")
    table.add_column("Carrera")
    for estudiante in datos["estudiantes"]:
        table.add_row(str(estudiante["id_estudiante"]), estudiante["nombre"], estudiante["carrera"])
    console.print(table)

def actualizar_estudiante():
    mostrar_estudiantes()
    datos = cargar_datos()
    
    while True:
        id_buscar = pedir_entero("Ingrese el ID del estudiante a actualizar")
        for estudiante in datos["estudiantes"]:
            if estudiante["id_estudiante"] == id_buscar:
                estudiante["nombre"] = pedir_texto("Ingrese el nuevo nombre")
                estudiante["carrera"] = pedir_texto("Ingrese la nueva carrera")
                guardar_datos(datos)
                console.print("[green]✔ Estudiante actualizado correctamente[/green]")
                return
        console.print("[red]✖ El ID de estudiante no existe. Intente de nuevo.[/red]")

def eliminar_estudiante():
    mostrar_estudiantes()
    datos = cargar_datos()
    
    while True:
        id_buscar = pedir_entero("Ingrese el ID del estudiante a eliminar")
        for estudiante in datos["estudiantes"]:
            if estudiante["id_estudiante"] == id_buscar:
                datos["estudiantes"].remove(estudiante)
                guardar_datos(datos)
                console.print("[green]✔ Estudiante eliminado correctamente[/green]")
                return
        console.print("[red]✖ El ID de estudiante no existe. Intente de nuevo.[/red]")


# --- CRUD CURSOS ---

def crear_curso():
    datos = cargar_datos()
    nombre = pedir_texto("Ingrese el nombre del curso")
    creditos = pedir_entero("Ingrese los créditos del curso")
    
    nuevo_id = 1
    for curso in datos["cursos"]:
        if curso["id_curso"] >= nuevo_id:
            nuevo_id = curso["id_curso"] + 1

    datos["cursos"].append({
        "id_curso": nuevo_id,
        "nombre_curso": nombre,
        "creditos": creditos
    })
    guardar_datos(datos)
    console.print(f"[green]✔ Curso creado con ID: {nuevo_id}[/green]")

def mostrar_cursos():
    datos = cargar_datos()
    if not datos["cursos"]:
        console.print("[yellow]No hay cursos registrados[/yellow]")
        return
    table = Table(title="Lista de Cursos")
    table.add_column("ID")
    table.add_column("Nombre del Curso")
    table.add_column("Créditos")
    for curso in datos["cursos"]:
        table.add_row(str(curso["id_curso"]), curso["nombre_curso"], str(curso["creditos"]))
    console.print(table)

def actualizar_curso():
    mostrar_cursos()
    datos = cargar_datos()
    
    while True:
        id_buscar = pedir_entero("Ingrese el ID del curso a actualizar")
        for curso in datos["cursos"]:
            if curso["id_curso"] == id_buscar:
                curso["nombre_curso"] = pedir_texto("Ingrese el nuevo nombre del curso")
                curso["creditos"] = pedir_entero("Ingrese los nuevos créditos")
                guardar_datos(datos)
                console.print("[green]✔ Curso actualizado correctamente[/green]")
                return
        console.print("[red]✖ El ID del curso no existe. Intente de nuevo.[/red]")

def eliminar_curso():
    mostrar_cursos()
    datos = cargar_datos()
    
    while True:
        id_buscar = pedir_entero("Ingrese el ID del curso a eliminar")
        for curso in datos["cursos"]:
            if curso["id_curso"] == id_buscar:
                datos["cursos"].remove(curso)
                guardar_datos(datos)
                console.print("[green]✔ Curso eliminado correctamente[/green]")
                return
        console.print("[red]✖ El ID del curso no existe. Intente de nuevo.[/red]")


# --- GESTIÓN DE MATRÍCULAS ---

def matricular_estudiante():
    mostrar_estudiantes()
    datos = cargar_datos()
    
    id_estudiante = None
    while True:
        id_buscar = pedir_entero("Ingrese el ID del estudiante a matricular")
        for estudiante in datos["estudiantes"]:
            if estudiante["id_estudiante"] == id_buscar:
                id_estudiante = id_buscar
                break
        if id_estudiante:
            break
        console.print("[red]✖ ID de estudiante no encontrado. Intente de nuevo.[/red]")

    mostrar_cursos()
    cantidad = pedir_entero("Ingrese la cantidad de cursos que va a matricular")
    lista_cursos = []
    
    for i in range(cantidad):
        while True:
            id_curso_individual = pedir_entero(f"Ingrese el ID del curso número {i+1}")
            existe_curso = False
            for curso in datos["cursos"]:
                if curso["id_curso"] == id_curso_individual:
                    existe_curso = True
                    break
            if existe_curso:
                if id_curso_individual not in lista_cursos:
                    lista_cursos.append(id_curso_individual)
                    break
                else:
                    console.print("[yellow]⚠ Este curso ya lo habías seleccionado para esta matrícula.[/yellow]")
            else:
                console.print("[red]✖ ID de curso no existe. Intente de nuevo.[/red]")

    periodo = pedir_texto("Ingrese el periodo académico")
    
    datos["matriculas"].append({
        "id_matricula": len(datos["matriculas"]) + 1,
        "id_estudiante": id_estudiante,
        "id_curso": lista_cursos,
        "periodo_academico": periodo
    })
    guardar_datos(datos)
    console.print("[green]✔ Matrícula registrada con éxito[/green]")


# --- CONSULTAS Y REPORTES ---

def ver_cursos_estudiante():
    mostrar_estudiantes()
    datos = cargar_datos()
    
    while True:
        id_estudiante = pedir_entero("Ingrese el ID del estudiante para ver sus cursos")
        existe_estudiante = False
        for estudiante in datos["estudiantes"]:
            if estudiante["id_estudiante"] == id_estudiante:
                existe_estudiante = True
                break
        if existe_estudiante:
            break
        console.print("[red]✖ El ID de estudiante no existe. Intente de nuevo.[/red]")
    
    encontrado = False
    for matricula in datos["matriculas"]:
        if matricula["id_estudiante"] == id_estudiante:
            encontrado = True
            table = Table(title=f"Cursos Matriculados - Periodo {matricula['periodo_academico']}")
            table.add_column("ID Curso")
            table.add_column("Nombre Curso")
            table.add_column("Créditos")
            
            for id_curso_individual in matricula["id_curso"]:
                for curso in datos["cursos"]:
                    if curso["id_curso"] == id_curso_individual:
                        table.add_row(str(curso["id_curso"]), curso["nombre_curso"], str(curso["creditos"]))
            console.print(table)
            
    if not encontrado:
        console.print("[yellow]⚠ El estudiante no tiene matrículas registradas.[/yellow]")

def ver_estudiantes_curso():
    mostrar_cursos()
    datos = cargar_datos()
    
    while True:
        id_curso = pedir_entero("Ingrese el ID del curso para ver sus estudiantes")
        existe_curso = False
        for curso in datos["cursos"]:
            if curso["id_curso"] == id_curso:
                existe_curso = True
                break
        if existe_curso:
            break
        console.print("[red]✖ El ID del curso no existe. Intente de nuevo.[/red]")
    
    table = Table(title="Aprendices Inscritos en el Curso")
    table.add_column("ID Estudiante")
    table.add_column("Nombre")
    table.add_column("Carrera")
    
    encontrado = False
    for matricula in datos["matriculas"]:
        if id_curso in matricula["id_curso"]:
            for estudiante in datos["estudiantes"]:
                if estudiante["id_estudiante"] == matricula["id_estudiante"]:
                    encontrado = True
                    table.add_row(str(estudiante["id_estudiante"]), estudiante["nombre"], estudiante["carrera"])
                    
    if encontrado:
        console.print(table)
    else:
        console.print("[yellow]⚠ No hay estudiantes matriculados en este curso.[/yellow]")

def total_creditos():
    mostrar_estudiantes()
    datos = cargar_datos()
    
    while True:
        id_estudiante = pedir_entero("Ingrese el ID del estudiante para calcular créditos")
        existe_estudiante = False
        for estudiante in datos["estudiantes"]:
            if estudiante["id_estudiante"] == id_estudiante:
                existe_estudiante = True
                break
        if existe_estudiante:
            break
        console.print("[red]✖ El ID de estudiante no existe. Intente de nuevo.[/red]")
    
    total = 0
    for matricula in datos["matriculas"]:
        if matricula["id_estudiante"] == id_estudiante:
            for id_curso_individual in matricula["id_curso"]:
                for curso in datos["cursos"]:
                    if curso["id_curso"] == id_curso_individual:
                        total += curso["creditos"]
                        
    console.print(f"[green]✔ El total de créditos matriculados es: {total}[/green]")