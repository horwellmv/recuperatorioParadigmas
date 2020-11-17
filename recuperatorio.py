import csv
import os.path

# -------------------- FUNCION PARA CREAR O SOBRE ESCRIBIR UN ARCHIVO .CSV --------------

def guardarLegajo(archivo, datos):
    guardar = "s"
    listLegajos = []

    while guardar == "s":
        legajo = {} # diccionario para agregar a lista de legajos
        try:
            for dato in datos:
                legajo[dato] = input(f"Ingrese {dato} : ")
            validar = int(legajo["legajo"]) # casteo a entero la clave ingresada como legajo.
            listLegajos.append(legajo)
            print("\tQuiere agregar otro legajo?")
            guardar = input("\ts/n :  ")
        except ValueError: # atrapo except al no poder castear string a entero.
            print("\tLegajo debe ser un entero. archivo cancelado.\n")
            return menu()

    try:
        yaExiste = os.path.isfile(archivo)  # METODO PARA BUSCAR ARCHIVO EXISTENTE
        with open(archivo, 'a', newline='') as file:
            file_guarda = csv.DictWriter(file, fieldnames=datos) # ENCABEZDOS DEL ARCHIVO

            if yaExiste:
                print("\tDesea sobreescribirlo?") # SI OPRIME S = OMITE EL ENCABEZADO Y AGREGA LOS NUEVOS LEGAJOS SIN BORRAR
                action = input("\t s/n: ")
                if action == "s":
                    file_guarda.writerows(listLegajos)
                else: return
            else:                # CREA ARCHIVO NUEVO CON ENCABEZADOS Y LEGAJOS
                file_guarda.writeheader()
                file_guarda.writerows(listLegajos)
                return

    except IOError:
        print("\tOcurrio un error con el archivo.")
        return

# ---------------------- FUNCION PARA CALCULAR LOS VIATICOS POR LEGAJO A BUSCAR --------------------------------

def mostrarLegajos(archivo1,archivo2, numeroLegajo):
    try:
        with open(archivo1) as fUser, open(archivo2) as fRecursos:
            usuarioCSv = csv.reader(fUser, delimiter = ",")
            recursosCSv = csv.reader(fRecursos, delimiter = ",")


            next(usuarioCSv)
            next(recursosCSv)

            legajo = next(usuarioCSv, None)
            gastos = next(recursosCSv, None)

            monto = 0
            limite = 5000
            nombre = ""

            while legajo: # mietras exista linea con legajo

                if int(legajo[0]) == numeroLegajo: # si legajo del archivo coincide con el de la busqueda
                    nombre = (f"{legajo[2]} {legajo[1]}") # rescato nombre asignado al legajo para mostrar en pantalla

                    while gastos: # recorro lista de recursos humanos con gastos de viaticos
                        if int(gastos[0])==numeroLegajo: # evaluo que coincide con el legajo buscado
                            monto = monto + int(gastos[1]) # sumo los valores que estan en el index 1 de gastos
                        gastos = next(recursosCSv, None) # paso de linea en archivo gastos
                legajo = next(usuarioCSv, None)

            if monto <= 5000:
                print(f"\tLegajo {numeroLegajo}: {nombre}, gastó {monto} \n \n")
            else:
                print(f"\tLegajo {numeroLegajo}: {nombre}, gastó {monto} y se ha pasado del presupuesto por {monto - limite}\n \n")
            return menu()
    except FileNotFoundError: # atrapo except en caso de no poder abrir archivo por error en nombre o por que no existe
        print(f"\tNo se pudo abrir el archivo{archivo1}, o el archivo no existe\n")
        return menu()

# ---------------------- MENU PRINCIPAL -------------------------------------------

def menu():
    datos = ["legajo", "apellido", "nombre"]
    archivoViaticos = []

    while True:
        print("  Menú: 1. Guardar legajos \n \t2. Consultar viaticos por legajo \n \t3. Exit")
        menu = input("\t")


        if menu == "1":
            print("\tIngrese nombre para su archivo \n\t(el .csv se agregarà por sistema):")
            print("\tO ingrese uno existente para agregar legajos \n\t")
            nombreArchivo = input("\t")
            guardarLegajo(f'\t{nombreArchivo}.csv', datos)


        if menu == "2":
            print("\tIngrese nombre del archivo a aparear sin la extension .csv:")
            nombreArchivo2 = input("\t")
            print("\tIngrese numero de legajo que quiere consultar: ")

            try:
                numeroRevisar = int(input("\t")) # evaluo que sea un entero el jegajo a buscar
                mostrarLegajos(f'\t{nombreArchivo2}.csv',"viaticos.csv",numeroRevisar)

            except ValueError:
                print("\tLegajo debe ser un entero. busqueda cancelada.\n")


        if menu == "3":
            exit()

        else:
            print("")


menu()
