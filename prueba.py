
mascotas = []
turnos_lista = []
servicios_realizados = []

id_mascota = 1
id_turno = 1

def volvermenu():
    input("\nPresione ENTER para volver al menú...")


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


def turnos():

    global id_turno

    try:

        id_mascota_buscar = int(input("Ingrese el ID de la mascota: "))

        encontrada = False

        for mascota in mascotas:

            if mascota["id"] == id_mascota_buscar:
                encontrada = True
                break

        if encontrada == False:

            print("La mascota no está registrada.")
            volvermenu()
            return

        fecha = input("Ingrese la fecha del turno: ")
        hora = input("Ingrese la hora del turno: ")

        for turno in turnos_lista:

            if turno["fecha"] == fecha and turno["hora"] == hora:

                print("Ese horario ya está ocupado.")
                volvermenu()
                return

        turno = {

            "id_turno": id_turno,
            "id_mascota": id_mascota_buscar,
            "fecha": fecha,
            "hora": hora,
            "realizado": False

        }

        turnos_lista.append(turno)

        print("\nTurno registrado correctamente.")
        print("ID del turno:", id_turno)

        id_turno += 1

        volvermenu()

    except ValueError:

        print("Debe ingresar datos válidos.")
        volvermenu()


def servicios():

    try:

        id_turno_buscar = int(input("Ingrese el ID del turno: "))

        turno_encontrado = None

        for turno in turnos_lista:

            if turno["id_turno"] == id_turno_buscar:

                turno_encontrado = turno
                break

        if turno_encontrado == None:

            print("No existe ese turno.")
            volvermenu()
            return

        if turno_encontrado["realizado"] == True:

            print("Ese turno ya fue utilizado.")
            volvermenu()
            return

        print("SERVICIOS")
        print("1. Baño")
        print("2. Peluquería")
        print("3. Venta de productos")
        print("4. Atención médica")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:

            servicio = "Baño"

        elif opcion == 2:

            servicio = "Peluquería"

        elif opcion == 3:

            servicio = "Venta de productos"

        elif opcion == 4:

            print("\nATENCIÓN MÉDICA")
            print("1. Vacunación")
            print("2. Control rutinario")
            print("3. Desparasitación")
            print("4. Cirugía")

            opcion_medica = int(input("Seleccione una opción: "))

            if opcion_medica == 1:

                servicio = "Vacunación"

            elif opcion_medica == 2:

                servicio = "Control rutinario"

            elif opcion_medica == 3:

                servicio = "Desparasitación"

            elif opcion_medica == 4:

                servicio = "Cirugía"

            else:

                print("Opción inválida.")
                volvermenu()
                return

        else:

            print("Opción inválida.")
            volvermenu()
            return

        observacion = input("Observaciones del servicio: ")

        servicio_realizado = {

            "id_turno": id_turno_buscar,
            "id_mascota": turno_encontrado["id_mascota"],
            "servicio": servicio,
            "observacion": observacion

        }

        servicios_realizados.append(servicio_realizado)

        turno_encontrado["realizado"] = True

        print("Servicio registrado correctamente.")

        volvermenu()

    except ValueError:

        print("Debe ingresar datos válidos.")
        volvermenu()


def estadisticas():

    if len(servicios_realizados) == 0:

        print("Todavía no hay servicios realizados.")
        volvermenu()
        return

    baños = 0
    peluquerias = 0
    productos = 0
    vacunaciones = 0
    controles = 0
    desparasitaciones = 0
    cirugias = 0

    print("\nSERVICIOS REALIZADOS")

    for servicio in servicios_realizados:

        print("---------------------")
        print("ID Mascota:", servicio["id_mascota"])
        print("Servicio:", servicio["servicio"])
        print("Observación:", servicio["observacion"])

        nombre_servicio = servicio["servicio"]

        if nombre_servicio == "Baño":
            baños += 1

        elif nombre_servicio == "Peluquería":
            peluquerias += 1

        elif nombre_servicio == "Venta de productos":
            productos += 1

        elif nombre_servicio == "Vacunación":
            vacunaciones += 1

        elif nombre_servicio == "Control rutinario":
            controles += 1

        elif nombre_servicio == "Desparasitación":
            desparasitaciones += 1

        elif nombre_servicio == "Cirugía":
            cirugias += 1

    print("\nESTADÍSTICAS")

    print("Mascotas registradas:", len(mascotas))
    print("Turnos registrados:", len(turnos_lista))
    print("Servicios realizados:", len(servicios_realizados))

    print("\nBaños realizados:", baños)
    print("Peluquerías realizadas:", peluquerias)
    print("Productos vendidos:", productos)
    print("Vacunaciones:", vacunaciones)
    print("Controles rutinarios:", controles)
    print("Desparasitaciones:", desparasitaciones)
    print("Cirugías:", cirugias)

    mayor = max(
        baños,
        peluquerias,
        productos,
        vacunaciones,
        controles,
        desparasitaciones,
        cirugias
    )

    if mayor == 0:

        servicio_mas_realizado = "Ninguno"

    elif mayor == vacunaciones:

        servicio_mas_realizado = "Vacunación"

    elif mayor == controles:

        servicio_mas_realizado = "Control rutinario"

    elif mayor == desparasitaciones:

        servicio_mas_realizado = "Desparasitación"

    elif mayor == cirugias:

        servicio_mas_realizado = "Cirugía"

    elif mayor == baños:

        servicio_mas_realizado = "Baño"

    elif mayor == peluquerias:

        servicio_mas_realizado = "Peluquería"

    else:

        servicio_mas_realizado = "Venta de productos"

    print("\nServicio más realizado:", servicio_mas_realizado)

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