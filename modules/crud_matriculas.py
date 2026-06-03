from guardar_cargar_datos import cargar_datos, guardar_datos
from rich import print # Importamos el print de rich para dar estilos

def matricular_estudiante():
    datos_matriculas = cargar_datos("data/matriculas.json")
    datos_estudiantes = cargar_datos("data/estudiantes.json")
    datos_cursos = cargar_datos("data/cursos.json")

    # 1. Validar ID Estudiante
    print("\n[bold cyan]--- LISTADO DE ESTUDIANTES ---[/bold cyan]")
    for e in datos_estudiantes:
        print(f"[cyan]ID:[/cyan] {e['id_estudiante']} | [cyan]Nombre:[/cyan] {e['nombre']}")

    id_estudiante = None
    while True:
        entrada = input("\nIngrese el ID del estudiante a matricular: ").strip()
        for est in datos_estudiantes:
            if str(est['id_estudiante']) == entrada:
                id_estudiante = entrada
                break
        
        if id_estudiante:
            break
        print("[bold red]Error:[/bold red] ID de estudiante no encontrado. Intente de nuevo.")

    # 2. Validar ID Curso
    print("\n[bold magenta]--- LISTADO DE CURSOS ---[/bold magenta]")
    for c in datos_cursos:
        print(f"[magenta]ID:[/magenta] {c['id_curso']} | [magenta]Curso:[/magenta] {c['nombre_curso']}")

    id_curso = None
    while True:
        entrada = input("\nIngrese el ID del curso: ").strip()
        for cur in datos_cursos:
            if str(cur['id_curso']) == entrada:
                id_curso = entrada
                break
        
        if id_curso:
            break
        print("[bold red]Error:[/bold red] ID de curso no encontrado. Intente de nuevo.")

    # 3. Validar si ya está matriculado
    for matricula in datos_matriculas:
        # Extraemos la lista de cursos y los convertimos a string para asegurar una buena comparación
        cursos_matriculados = [str(curso) for curso in matricula['id_curso']]
        
        # Verificamos si el ID del estudiante coincide Y si el ID del curso está dentro de su lista
        if str(matricula['id_estudiante']) == id_estudiante and id_curso in cursos_matriculados:
            print("[bold yellow]Error:[/bold yellow] El estudiante ya está matriculado en este curso.")
            return
        
    # Pedimos el periodo académico FUERA del bucle for
    periodo_academico = input("\nIngrese el periodo académico (e.g., 2026-2): ").strip()

    # 4. Guardar
    nueva_matricula = {
        "id_matricula": len(datos_matriculas) + 1,
        "id_estudiante": int(id_estudiante),
        "id_curso": [int(id_curso)],
        "periodo_academico": periodo_academico
    }

    datos_matriculas.append(nueva_matricula)
    guardar_datos("data/matriculas.json", datos_matriculas)
    print(f"\n[bold green]¡Éxito![/bold green] Estudiante [bold]{id_estudiante}[/bold] matriculado correctamente en el curso [bold]{id_curso}[/bold].")

matricular_estudiante()