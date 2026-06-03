import json
from rich.console import Console 
console = Console()

# ---GUARDADO DE DATOS ---
def guardar_datos(archivo_json, datos): # se debe poner un archivo json y los datos a guardar en formato de diccionario
    try:
        with open(archivo_json, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4)
        console.print("[bold green]✔ Datos guardados correctamente[/bold green]")
    except Exception:
        console.print("[red]✖ Ocurrio un error al guardar los datos[/red]")

# ---CARGAR DATOS ---
def cargar_datos(archivo_json):#ingresar el archivo json al cual se desea cargar
    try:
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        console.print("[yellow]⚠ Archivo no encontrado[/yellow]")
        return {"estudiantes": [], "cursos": [], "matriculas": []}  #debuelve un diccionario anidado vacio

#guardar_datos("Entidades/matriculas.json", matriculas) ejemplo de como se debe introducir parametros para guardar datos
#cargar_datos("Entidades/matriculas.json") # ejemplo de como se debe introducir parametros para cargar datos
#cargar datos no imprime nada