while True:

    print("\n-------------------")
    print(" Veterinaria Patitas")
    print("-------------------")
    print("Bienvenidos/as a la Veterinaria Patitas")
    print("1. Registrar a su mascota")
    print("2. Solicitar un turno")
    print("3. Servicios")
    print("4. Visualizar servicios realizados y estadísticas")
    print("5. Salir")

    try:

        opcion = int(input("Seleccionar una opción: "))

        if opcion == 1:

            registrarmascota()

        elif opcion == 2:

            turnos()

        elif opcion == 3:

            servicios()

        elif opcion == 4:

            estadisticas()

        elif opcion == 5:

            print("\nGracias por visitar la Veterinaria Patitas.")
            break

        else:

            print("Opción no válida.")
            volvermenu()

    except ValueError:

        print("Debe ingresar un número.")
        volvermenu()