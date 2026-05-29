import json

#FUNCION PARA GUARDAR LOS DATOS EN EL ARCHIVO JSON
def guardar_datos(datos):
    with open("datos_entidades.json", "w") as file:
        json.dump(datos , file, indent=2 ,ensure_ascii=False)

#FUNCION PARA VER LISTA DE CURSOS DE UN ESTUDIANTE
def lista_cursos_estudiante(): 
    with open("datos_entidades.json", "r") as file:
        lista=json.load(file)#guardamos todos los registros en una variable

    #IMPRIMIR ESTUDIANTES REGISTRADOS
    print("========ESTUDIANTES========")
    for estudiante in lista["estudiantes"]:
        print(f"{estudiante["nombre"]} ")
    print("===========================")
    
    estudiante_elegido = input("Ingrese un estudiante: ")

    id_estudiante=0
    #REVISAR SI EL ESTUDIANTE EXISTE 
    while True:
        # variable para validar si se encontro o no
        encontrado = False
        
        # buscamos el nombre
        for estudiante in lista["estudiantes"]:
            if estudiante_elegido.lower() == estudiante["nombre"].lower():
                #SI EL ESTUDIANTE EXISTE, TOMAMOS SU ID
                id_estudiante=int(estudiante["id_estudiante"])
                encontrado = True
                break  
                
        # revisamos el resultado de la busqueda
        if encontrado:
            break  
        else:
            print("ERROR: Este estudiante no existe en la lista. Intente de nuevo.")
            estudiante_elegido = input("Ingrese un estudiante: ")
        
    #BUSCAR EL ID DEL ESTUDIANTE EN LAS MATRICULAS
    print("========CURSOS DEL ESTUDIANTE========")
    for datos in lista["matriculas"]:
        if id_estudiante == datos["id_estudiante"]:
            id_cursos = datos["id_curso"] #guardamos los cursos en los que esra inscrito el estudiante
            
            #BUSCAMOS LOS CURSOS EN LOS QUE ESTA INSCRITO
            for curso in lista["cursos"]:
                #verificamos si el id del curso esta o no 
                if curso["id_curso"] in id_cursos:
                    print(f"{curso['nombre_curso']}")
            break
    #en caso de que no este matriculado
        else:
            print("El estudiante no esta matriculado en ningun curso")
