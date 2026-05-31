from funciones import (
    crear_estudiante, listar_estudiantes,
    crear_curso, listar_cursos,
    registrar_matricula, listar_matriculas,
    lista_cursos_estudiante, calcular_creditos
)

def menu():
    while True:
        print("\n--- Sistema de Gestión de Matrículas ---")
        print("1. Crear estudiante")
        print("2. Listar estudiantes")
        print("3. Crear curso")
        print("4. Listar cursos")
        print("5. Registrar matrícula")
        print("6. Listar matrículas")
        print("7. Ver cursos de un estudiante")
        print("8. Calcular créditos de un estudiante")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_estudiante()
        elif opcion == "2":
            listar_estudiantes()
        elif opcion == "3":
            crear_curso()
        elif opcion == "4":
            listar_cursos()
        elif opcion == "5":
            registrar_matricula()
        elif opcion == "6":
            listar_matriculas()
        elif opcion == "7":
            lista_cursos_estudiante()
        elif opcion == "8":
            try:
                id_est = int(input("Ingrese el ID del estudiante: "))
                calcular_creditos(id_est)
            except ValueError:
                print("Error: el ID debe ser un número.")
        elif opcion == "9":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

menu()
