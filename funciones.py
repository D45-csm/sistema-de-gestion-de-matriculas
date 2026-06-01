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

# ==========================================
# FUNCIONES DE AYUDA (VALIDACIÓN Y ROBUSTEZ)
# ==========================================

def pedir_cadena(mensaje):
    """Pide un texto y no permite que esté vacío. Permite salir."""
    while True:
        valor = input(f"{mensaje} (o 'salir' para cancelar): ").strip()
        if valor.lower() == 'salir':
            return None
        if valor:
            return valor
        console.print("[yellow]⚠ El campo no puede estar vacío.[/yellow]")

def pedir_entero(mensaje):
    """Pide un número y vuelve a preguntar si el usuario se equivoca. Permite salir."""
    while True:
        valor = input(f"{mensaje} (o 'salir' para cancelar): ").strip()
        if valor.lower() == 'salir':
            return None
        try:
            return int(valor)
        except ValueError:
            console.print("[red]✖ Por favor, ingrese un número entero válido.[/red]")

def generar_nuevo_id(lista, campo_id):
    """Genera un ID seguro basado en el máximo existente, evitando colisiones si se borran datos."""
    if not lista:
        return 1
    return max(item[campo_id] for item in lista) + 1

# ==========================================
# CRUD ESTUDIANTES
# ==========================================

def mostrar_estudiantes():
    datos = cargar_datos()
    estudiantes = datos["estudiantes"]
    if len(estudiantes) == 0:
        console.print("[yellow]No hay estudiantes registrados[/yellow]")
        return False # Retorna False para saber si hay datos para operar

    table = Table(title="Lista de Estudiantes")
    table.add_column("ID", justify="center")
    table.add_column("Nombre")
    table.add_column("Carrera")

    for estudiante in estudiantes:
        table.add_row(
            str(estudiante["id_estudiante"]),
            estudiante["nombre"],
            estudiante["carrera"]
        )
    console.print(table)
    return True

def crear_estudiante():
    datos = cargar_datos()
    
    nombre = pedir_cadena("Nombre")
    if not nombre: return
    
    # Validar duplicados
    if any(e["nombre"].lower() == nombre.lower() for e in datos["estudiantes"]):
        console.print("[yellow]⚠ Ya existe un estudiante con ese nombre.[/yellow]")
        return

    carrera = pedir_cadena("Carrera")
    if not carrera: return

    nuevo_id = generar_nuevo_id(datos["estudiantes"], "id_estudiante")
    
    datos["estudiantes"].append({
        "id_estudiante": nuevo_id,
        "nombre": nombre,
        "carrera": carrera
    })
    guardar_datos(datos)
    console.print("[green]✔ Estudiante creado correctamente[/green]")

def actualizar_estudiante():
    if not mostrar_estudiantes(): return
    datos = cargar_datos()
    
    while True:
        id_estudiante = pedir_entero("Ingrese ID estudiante a actualizar")
        if id_estudiante is None: return

        for estudiante in datos["estudiantes"]:
            if estudiante["id_estudiante"] == id_estudiante:
                nuevo_nombre = pedir_cadena(f"Nuevo nombre (actual: {estudiante['nombre']})")
                if not nuevo_nombre: return
                
                nueva_carrera = pedir_cadena(f"Nueva carrera (actual: {estudiante['carrera']})")
                if not nueva_carrera: return

                estudiante["nombre"] = nuevo_nombre
                estudiante["carrera"] = nueva_carrera
                guardar_datos(datos)
                console.print("[green]✔ Estudiante actualizado correctamente[/green]")
                return
        console.print("[yellow]⚠ ID de estudiante no encontrado. Intente de nuevo.[/yellow]")

def eliminar_estudiante():
    if not mostrar_estudiantes(): return
    datos = cargar_datos()
    
    while True:
        id_estudiante = pedir_entero("Ingrese ID estudiante a eliminar")
        if id_estudiante is None: return

        for estudiante in datos["estudiantes"]:
            if estudiante["id_estudiante"] == id_estudiante:
                datos["estudiantes"].remove(estudiante)
                guardar_datos(datos)
                console.print("[green]✔ Estudiante eliminado correctamente[/green]")
                return
        console.print("[yellow]⚠ ID de estudiante no encontrado. Intente de nuevo.[/yellow]")


# ==========================================
# CRUD CURSOS
# ==========================================

def mostrar_cursos():
    datos = cargar_datos()
    cursos = datos["cursos"]
    if len(cursos) == 0:
        console.print("[yellow]No hay cursos registrados[/yellow]")
        return False
        
    table = Table(title="Lista de Cursos")
    table.add_column("ID", justify="center")
    table.add_column("Nombre")
    table.add_column("Creditos", justify="center")
    
    for curso in cursos:
        table.add_row(
            str(curso["id_curso"]),
            curso["nombre_curso"],
            str(curso["creditos"])
        )
    console.print(table)
    return True

def crear_curso():
    datos = cargar_datos()
    
    nombre_curso = pedir_cadena("Nombre del curso")
    if not nombre_curso: return
    
    if any(c["nombre_curso"].lower() == nombre_curso.lower() for c in datos["cursos"]):
        console.print("[yellow]⚠ Ya existe un curso con ese nombre.[/yellow]")
        return

    creditos = pedir_entero("Creditos")
    if creditos is None: return

    nuevo_id = generar_nuevo_id(datos["cursos"], "id_curso")
    
    datos["cursos"].append({
        "id_curso": nuevo_id,
        "nombre_curso": nombre_curso,
        "creditos": creditos
    })
    guardar_datos(datos)
    console.print("[green]✔ Curso creado correctamente[/green]")

def actualizar_curso():
    if not mostrar_cursos(): return
    datos = cargar_datos()
    
    while True:
        id_curso = pedir_entero("Ingrese ID del curso a actualizar")
        if id_curso is None: return

        for curso in datos["cursos"]:
            if curso["id_curso"] == id_curso:
                nuevo_nombre = pedir_cadena(f"Nuevo nombre (actual: {curso['nombre_curso']})")
                if not nuevo_nombre: return
                
                nuevos_creditos = pedir_entero(f"Nuevos creditos (actual: {curso['creditos']})")
                if nuevos_creditos is None: return

                curso["nombre_curso"] = nuevo_nombre
                curso["creditos"] = nuevos_creditos
                guardar_datos(datos)
                console.print("[green]✔ Curso actualizado correctamente[/green]")
                return
        console.print("[yellow]⚠ Curso no encontrado. Intente de nuevo.[/yellow]")

def eliminar_curso():
    if not mostrar_cursos(): return
    datos = cargar_datos()
    
    while True:
        id_curso = pedir_entero("Ingrese ID del curso a eliminar")
        if id_curso is None: return

        for curso in datos["cursos"]:
            if curso["id_curso"] == id_curso:
                datos["cursos"].remove(curso)
                guardar_datos(datos)
                console.print("[green]✔ Curso eliminado correctamente[/green]")
                return
        console.print("[yellow]⚠ Curso no encontrado. Intente de nuevo.[/yellow]")

# ==========================================
# OPERACIONES Y RETOS
# ==========================================

def matricular_estudiante():
    if not mostrar_estudiantes(): return
    datos = cargar_datos()
    
    while True:
        id_estudiante = pedir_entero("Ingrese ID del estudiante")
        if id_estudiante is None: return
        if any(e["id_estudiante"] == id_estudiante for e in datos["estudiantes"]):
            break
        console.print("[yellow]⚠ Estudiante no existe. Intente de nuevo.[/yellow]")

    if not mostrar_cursos(): return
    
    cantidad = pedir_entero("Cantidad de cursos a matricular")
    if cantidad is None: return
    
    lista_cursos = []
    for numero in range(cantidad):
        while True:
            id_curso = pedir_entero(f"Ingrese ID del curso #{numero+1}")
            if id_curso is None: return
            
            if not any(c["id_curso"] == id_curso for c in datos["cursos"]):
                console.print("[yellow]⚠ El curso no existe. Intente de nuevo.[/yellow]")
            elif id_curso in lista_cursos:
                console.print("[yellow]⚠ Ya agregó este curso a la matrícula.[/yellow]")
            else:
                lista_cursos.append(id_curso)
                break

    periodo = pedir_cadena("Periodo académico")
    if not periodo: return

    nuevo_id_matricula = generar_nuevo_id(datos["matriculas"], "id_matricula")
    
    datos["matriculas"].append({
        "id_matricula": nuevo_id_matricula,
        "id_estudiante": id_estudiante,
        "id_curso": lista_cursos,
        "periodo_academico": periodo
    })
    guardar_datos(datos)
    console.print("[green]✔ Matrícula registrada correctamente[/green]")

def ver_cursos_estudiante():
    if not mostrar_estudiantes(): return
    datos = cargar_datos()
    
    while True:
        id_estudiante = pedir_entero("Ingrese ID del estudiante para ver sus cursos")
        if id_estudiante is None: return
        if any(e["id_estudiante"] == id_estudiante for e in datos["estudiantes"]):
            break
        console.print("[yellow]⚠ Estudiante no encontrado.[/yellow]")

    encontrado = False
    for matricula in datos["matriculas"]:
        if matricula["id_estudiante"] == id_estudiante:
            encontrado = True
            table = Table(title=f"Cursos del Estudiante (Periodo: {matricula['periodo_academico']})")
            table.add_column("Cursos")
            for curso in datos["cursos"]:
                if curso["id_curso"] in matricula["id_curso"]:
                    table.add_row(curso["nombre_curso"])
            console.print(table)
            
    if not encontrado:
        console.print("[yellow]⚠ El estudiante no tiene cursos matriculados[/yellow]")

def ver_estudiantes_curso():
    if not mostrar_cursos(): return
    datos = cargar_datos()
    
    while True:
        id_curso = pedir_entero("Ingrese ID del curso para ver sus estudiantes")
        if id_curso is None: return
        if any(c["id_curso"] == id_curso for c in datos["cursos"]):
            break
        console.print("[yellow]⚠ Curso no encontrado.[/yellow]")

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
        console.print("[yellow]⚠ No hay estudiantes matriculados en este curso[/yellow]")

def total_creditos():
    if not mostrar_estudiantes(): return
    datos = cargar_datos()
    
    while True:
        id_estudiante = pedir_entero("Ingrese ID del estudiante para calcular créditos")
        if id_estudiante is None: return
        if any(e["id_estudiante"] == id_estudiante for e in datos["estudiantes"]):
            break
        console.print("[yellow]⚠ Estudiante no encontrado.[/yellow]")

    total = 0
    for matricula in datos["matriculas"]:
        if matricula["id_estudiante"] == id_estudiante:
            for id_curso in matricula["id_curso"]:
                for curso in datos["cursos"]:
                    if curso["id_curso"] == id_curso:
                        total += curso["creditos"]
                        
    console.print(f"[green]✔ Total de creditos acumulados: {total}[/green]")