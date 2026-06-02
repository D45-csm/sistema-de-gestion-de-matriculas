import json
import os 

# ruta de archivos de datos
RUTA_CURSOS = os.path.join("data", "cursos.json")

#========================
#FUNCIONES AUXILIARES 
#========================
def cargar_cursos():
    if not os.path.exists(RUTA_CURSOS):
        return []
    with open(RUTA_CURSOS, "r", encoding="utf-8") as file:
        return json.load(file)

def guardar_cursos(cursos):
    with open(RUTA_CURSOS, "w", encoding="utf-8") as file:
        json.dump(cursos, file, indent=2, ensure_ascii=False)
            
#========================
#CRUD DE CURSOS
#========================
 
def crear_curso():
    cursos = cargar_cursos()
    id_curso = int(input("Ingrese el ID del curso: "))
    nombre = input("Ingrese el nombre del curso: ")
    creditos = int(input("Ingrese la cantidad de creditos: "))

    nuevo_curso = {
        "id_curso": id_curso,
        "nombre_curso": nombre,
        "creditos": creditos
    }
    cursos.append(nuevo_curso)
    guardar_cursos(cursos)
    print("Curso creado correctamente.")
   