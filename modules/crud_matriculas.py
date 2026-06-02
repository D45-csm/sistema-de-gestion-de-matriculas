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

""" def mostrar_estudiantes():
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
        console.print("[red]✖ El ID de estudiante no existe. Intente de nuevo.[/red]") """