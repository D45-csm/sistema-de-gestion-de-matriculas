import os
import json
from typing import List, Dict, Optional
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# ==========================
# Configuración inicial
# ==========================
console = Console()

# Rutas de archivos JSON (base de datos)
RUTA_CURSOS = os.path.join("data", "cursos.json")
RUTA_ESTUDIANTES = os.path.join("data", "estudiantes.json")
RUTA_MATRICULAS = os.path.join("data", "matriculas.json")

# ==========================
# Funciones de carga y guardado
# ==========================
def cargar_datos(ruta: str) -> List[Dict]:
    """Carga datos desde un archivo JSON. Devuelve lista vacía si no existe o está dañado."""
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
            return json.loads(contenido) if contenido else []
    except json.JSONDecodeError:
        return []

def guardar_datos(ruta: str, datos: List[Dict]) -> None:
    """Guarda datos en formato JSON con indentación y UTF-8."""
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

# ==========================
# Funciones auxiliares
# ==========================
def buscar_curso(cursos: List[Dict], id_curso: int) -> Optional[Dict]:
    """Busca un curso por su ID."""
    return next((c for c in cursos if c["id_curso"] == id_curso), None)

def mostrar_tabla(titulo: str, columnas: List[str], filas: List[List[str]]) -> None:
    """Muestra una tabla en consola con Rich."""
    tabla = Table(title=titulo, show_lines=True, header_style="bold cyan", title_style="bold magenta")
    for col in columnas:
        tabla.add_column(col, justify="center")
    for fila in filas:
        tabla.add_row(*fila)
    console.print(tabla)

# ==========================
# CRUD de Cursos
# ==========================
def crear_curso() -> None:
    cursos = cargar_datos(RUTA_CURSOS)
    try:
        id_curso = int(input("Ingrese el ID del curso: "))
        if buscar_curso(cursos, id_curso):
            console.print("[red]⚠ Ya existe un curso con ese ID.[/red]")
            return

        nombre = input("Ingrese el nombre del curso: ").strip()
        creditos = int(input("Ingrese la cantidad de créditos: "))

        cursos.append({"id_curso": id_curso, "nombre_curso": nombre, "creditos": creditos})
        guardar_datos(RUTA_CURSOS, cursos)
        console.print("[green]✔ Curso creado correctamente.[/green]")
    except ValueError:
        console.print("[red]✖ Entrada inválida. Use números para ID y créditos.[/red]")

def listar_cursos() -> None:
    cursos = cargar_datos(RUTA_CURSOS)
    if not cursos:
        console.print("[yellow]⚠ No hay cursos registrados.[/yellow]")
        return
    filas = [[str(c["id_curso"]), c["nombre_curso"], str(c["creditos"])] for c in cursos]
    mostrar_tabla("📚 LISTA DE CURSOS", ["ID", "Nombre del curso", "Créditos"], filas)

def actualizar_curso() -> None:
    cursos = cargar_datos(RUTA_CURSOS)
    try:
        id_curso = int(input("Ingrese el ID del curso a actualizar: "))
        curso = buscar_curso(cursos, id_curso)
        if not curso:
            console.print("[red]❌ Curso no encontrado.[/red]")
            return

        curso["nombre_curso"] = input("Nuevo nombre del curso: ").strip()
        curso["creditos"] = int(input("Nuevos créditos: "))
        guardar_datos(RUTA_CURSOS, cursos)
        console.print("[green]✔ Curso actualizado correctamente.[/green]")
    except ValueError:
        console.print("[red]✖ Entrada inválida. Use números para ID y créditos.[/red]")

def eliminar_curso() -> None:
    cursos = cargar_datos(RUTA_CURSOS)
    try:
        id_curso = int(input("Ingrese el ID del curso a eliminar: "))
        curso = buscar_curso(cursos, id_curso)
        if not curso:
            console.print("[red]❌ Curso no encontrado.[/red]")
            return

        cursos = [c for c in cursos if c["id_curso"] != id_curso]
        guardar_datos(RUTA_CURSOS, cursos)
        console.print("[green]🗑️ Curso eliminado correctamente.[/green]")
    except ValueError:
        console.print("[red]✖ Entrada inválida. Use números para ID.[/red]")

# ==========================
# Consultas
# ==========================
def ver_estudiantes_de_curso() -> None:
    """Muestra los estudiantes matriculados en un curso específico."""
    cursos = cargar_datos(RUTA_CURSOS)
    estudiantes = cargar_datos(RUTA_ESTUDIANTES)
    matriculas = cargar_datos(RUTA_MATRICULAS)

    try:
        id_curso = int(input("Ingrese el ID del curso: "))
        curso = buscar_curso(cursos, id_curso)
        if not curso:
            console.print("[red]❌ Curso no encontrado.[/red]")
            return

        console.print(Panel(f"👩‍🏫 Estudiantes en [bold cyan]{curso['nombre_curso']}[/bold cyan]",
                            border_style="cyan", title="Información del curso"))

        # Buscar estudiantes matriculados en el curso
        encontrados = [
            next((e for e in estudiantes if e["id_estudiante"] == m["id_estudiante"]), None)
            for m in matriculas
            if (
                isinstance(m.get("id_curso"), list) and id_curso in m["id_curso"]
            ) or m.get("id_curso") == id_curso
        ]
        encontrados = [e for e in encontrados if e]

        if encontrados:
            contenido = "\n".join(
                [f"🧑‍🎓 [bold blue]{e['nombre']}[/bold blue] | Carrera: [magenta]{e['carrera']}[/magenta] | ID: [bold]{e['id_estudiante']}[/bold]"
                 for e in encontrados]
            )
            console.print(Panel(contenido, title="✅ Estudiantes encontrados", border_style="green"))
        else:
            console.print(Panel("⚠ Ningún estudiante está matriculado en este curso.",
                                border_style="yellow", title="Sin resultados"))
    except ValueError:
        console.print("[red]✖ Entrada inválida. Use números para ID.[/red]")

# ==========================
# Menú
# ==========================
def menu_gestion_cursos():
    """Menú principal para gestionar cursos."""
    opciones = {
        "1": crear_curso,
        "2": listar_cursos,
        "3": actualizar_curso,
        "4": eliminar_curso,
        "5": ver_estudiantes_de_curso
    }

    while True:
        menu_texto = (
            "[bold cyan]1.[/bold cyan] Crear curso\n"
            "[bold cyan]2.[/bold cyan] Ver lista de cursos\n"
            "[bold cyan]3.[/bold cyan] Actualizar curso\n"
            "[bold cyan]4.[/bold cyan] Eliminar curso\n"
            "[bold cyan]5.[/bold cyan] Ver estudiantes de un curso\n"
            "[bold cyan]6.[/bold cyan] Volver al menú principal"
        )
        console.print(Panel(menu_texto, title="[bold cyan]💼 GESTIÓN DE CURSOS[/bold cyan]", border_style="cyan", width=55))
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "6":
            break
        accion = opciones.get(opcion)
        accion() if accion else console.print("[bold red]Opción no válida.[/bold red]")

if __name__ == "__main__":
    menu_gestion_cursos()
