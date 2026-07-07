mascotas = []
turnos_lista = []
servicios_realizados = []

id_mascota = 1
id_turno = 1

def volvermenu():
    input("\nPresione enter para volver al menú")


def registrarmascota():

    global id_mascota

    nombre = input("Nombre de la mascota: ")
    especie = input("Especie: ")

    try:

        edad = int(input("Edad: "))

    except ValueError:

        print("La edad debe ser un número.")
        volvermenu()
        return

    if edad <= 0:

        print("La edad debe ser mayor a 0.")
        volvermenu()
        return

    dueño = input("Nombre del dueño: ")

    try:

        telefono = int(input("Teléfono: "))

    except ValueError:

        print("El teléfono debe ser un número.")
        volvermenu()
        return

    for mascota in mascotas:

        if (mascota["nombre"] == nombre
            and mascota["especie"] == especie
            and mascota["edad"] == edad):

            print("La mascota ya está registrada.")
            volvermenu()
            return

    mascota = {

        "id": id_mascota,
        "nombre": nombre,
        "especie": especie,
        "edad": edad,
        "dueño": dueño,
        "telefono": telefono

    }

    mascotas.append(mascota)

    print("\nMascota registrada correctamente.")
    print("ID asignado:", id_mascota)

    id_mascota += 1

    volvermenu()



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