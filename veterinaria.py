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

def servicios():
    try:
        id_turno_buscar = int(input("ingrese el ID del turno: "))
        turno_encontrado = None
        for turno in turnos_lista:
            if turno["id_turno"] == id_turno_buscar:
                turno_encontrado == turno
                break
        if turno_encontrado == None:
            print("no existe ese turno")
            volvermenu()
            return
        if turno_encontrado["realizado"] == True:
            print("ese turno ya esta ocupado")
            volvermenu()
            return
        print("SERVICIOS")
        print("1. Baño")
        print("2. Peluqueria")
        print("3. Venta de productos")
        print("4. Atencion Medica")
        opcion = int(input("seleccione una opcion: "))
        if opcion == 1:
            servicio == "Baño"
        elif opcion == 2:
            servicio == "Peluqueria"
        elif opcion == 3:
            servicio == "Venta de productos"
        elif opcion == 4:
            print("\nATENCIÓN MÉDICA")
            print("1. Vacunación")
            print("2. Control rutinario")
            print("3. Desparasitación")
            print("4. Cirugía")
            


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