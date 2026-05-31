import json

# ==========================
# FUNCIONES AUXILIARES
# ==========================

# Guardar datos en JSON
def guardar_datos(datos):
    with open("datos_entidades.json", "w") as file:
        json.dump(datos, file, indent=2, ensure_ascii=False)

# Cargar datos desde JSON
def cargar_datos():
    try:
        with open("datos_entidades.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"estudiantes": [], "cursos": [], "matriculas": []}

# ==========================
# CRUD ESTUDIANTES
# ==========================

def crear_estudiante():
    datos = cargar_datos()
    nuevo = {
        "id_estudiante": len(datos["estudiantes"]) + 1,
        "nombre": input("Nombre: "),
        "carrera": input("Carrera: ")
    }
    datos["estudiantes"].append(nuevo)
    guardar_datos(datos)
    print("Estudiante registrado.")

def listar_estudiantes():
    datos = cargar_datos()
    print("======== ESTUDIANTES ========")
    for e in datos["estudiantes"]:
        print(f"ID: {e['id_estudiante']} | Nombre: {e['nombre']} | Carrera: {e['carrera']}")
    print("=============================")

# ==========================
# CRUD CURSOS
# ==========================

def crear_curso():
    datos = cargar_datos()
    nuevo = {
        "id_curso": int(input("ID del curso: ")),
        "nombre_curso": input("Nombre del curso: "),
        "creditos": int(input("Créditos: "))
    }
    datos["cursos"].append(nuevo)
    guardar_datos(datos)
    print("Curso registrado.")

def listar_cursos():
    datos = cargar_datos()
    print("======== CURSOS ========")
    for c in datos["cursos"]:
        print(f"ID: {c['id_curso']} | Nombre: {c['nombre_curso']} | Créditos: {c['creditos']}")
    print("========================")

# ==========================
# CRUD MATRÍCULAS
# ==========================

def registrar_matricula():
    datos = cargar_datos()
    nueva = {
        "id_matricula": len(datos["matriculas"]) + 1,
        "id_estudiante": int(input("ID del estudiante: ")),
        "id_curso": [int(x) for x in input("IDs de cursos separados por coma: ").split(",")],
        "periodo_academico": input("Periodo académico: ")
    }
    datos["matriculas"].append(nueva)
    guardar_datos(datos)
    print("Matrícula registrada.")

def listar_matriculas():
    datos = cargar_datos()
    print("======== MATRÍCULAS ========")
    for m in datos["matriculas"]:
        print(f"ID Matrícula: {m['id_matricula']} | Estudiante: {m['id_estudiante']} | Cursos: {m['id_curso']} | Periodo: {m['periodo_academico']}")
    print("============================")

# ==========================
# CONSULTAS
# ==========================

def lista_cursos_estudiante():
    datos = cargar_datos()

    print("======== ESTUDIANTES ========")
    for estudiante in datos["estudiantes"]:
        print(f"{estudiante['nombre']}")
    print("=============================")

    estudiante_elegido = input("Ingrese un estudiante: ")
    id_estudiante = None

    for estudiante in datos["estudiantes"]:
        if estudiante_elegido.lower() == estudiante["nombre"].lower():
            id_estudiante = estudiante["id_estudiante"]
            break

    if id_estudiante is None:
        print("Estudiante no encontrado.")
        return

    print("======== CURSOS DEL ESTUDIANTE ========")
    encontrado = False
    for m in datos["matriculas"]:
        if m["id_estudiante"] == id_estudiante:
            for curso in datos["cursos"]:
                if curso["id_curso"] in m["id_curso"]:
                    print(f"{curso['nombre_curso']}")
            encontrado = True
            break

    if not encontrado:
        print("El estudiante no está matriculado en ningún curso.")

def calcular_creditos(id_estudiante):
    datos = cargar_datos()
    total = 0
    for m in datos["matriculas"]:
        if m["id_estudiante"] == id_estudiante:
            for id_curso in m["id_curso"]:
                for c in datos["cursos"]:
                    if c["id_curso"] == id_curso:
                        total += c["creditos"]
    print(f"Total de créditos matriculados: {total}")
