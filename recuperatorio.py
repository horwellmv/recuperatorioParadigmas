import csv
import os.path



def guardarLegajo(archivo, datos):
    guardar = "s"
    listLegajos = []

    while guardar == "s":
        legajo = {}

        for dato in datos:
            legajo[dato] = input(f"Ingrese {dato} : ")
        listLegajos.append(legajo)
        print("\tQuiere agregar otro legajo?")
        guardar = input("\ts/n :  ")

    try:
        yaExiste = os.path.isfile(archivo)
        with open(archivo, 'a', newline='') as file:
            file_guarda = csv.DictWriter(file, fieldnames=datos)

            if yaExiste:
                print("\tDesea sobreescribirlo?")
                action = input("\t s/n: ")
                if action == "s":
                    file_guarda.writerows(listLegajos)
                else: return
            else:
                file_guarda.writeheader()
                file_guarda.writerows(listLegajos)
                return

    except IOError:
        print("\tOcurrio un error con el archivo.")
        return





def mostrarLegajos(archivo1,archivo2, numeroLegajo):
    with open(archivo1) as fUser, open(archivo2) as fRecursos:
            usuarioCSv = csv.reader(fUser, delimiter = ",")
            recursosCSv = csv.reader(fRecursos, delimiter = ",")


            next(usuarioCSv)
            next(recursosCSv)

            legajo = next(usuarioCSv, None)
            gastos = next(recursosCSv, None)

            monto = 0
            limite = 5000 - monto
            print(numeroLegajo)
            print(legajo)

            while int(legajo[0]) == numeroLegajo:

                print(f"{legajo[0]}, pertenece a {legajo[1]} {legajo[2]}")
                if not gastos or gastos[0] != legajo[0]:
                    print("\tNo hay regisros para este usuario")

                while gastos and gastos[0] == legajo[0]:
                    print(f"\t{legajo[1]} tiene $: {gastos[1]}")
                    monto = monto + int(gastos[1])
                    gastos = next(recursosCSv, None)

            if monto <= 5000:
                print(f'\tMonto de viaticos usados por {legajo[1]} {legajo[2]} es de {monto} ')

            else:
                print(f"\tMonto de viaticos usados por {legajo[1]} {legajo[2]} es de {monto} y supero por {limite}")























def menu():
    datos = ["legajo", "apellido", "nombre"]
    archivoViaticos = []

    while True:
        print("  Menú: 1. Guardar legajo \n \t2. Mostrar legajos \n \t3. Exit")
        menu = input("\t")


        if menu == "1":
            print("\tIngrese nombre para su archivo:")
            nombreArchivo = input("\t")
            guardarLegajo(f'\t{nombreArchivo}.csv', datos)

        if menu == "2":
            print("\tIngrese nombre del archivo a aparear sin .csv:")
            nombreArchivo2 = input("\t")
            print("\tIngrese numero de legajo a revisar: ")
            numeroRevisar = int(input("\t"))
            mostrarLegajos(f'\t{nombreArchivo2}.csv',"viaticos.csv",numeroRevisar)

        if menu == "3":
            exit()

        else: print("\tRegreso a Menu!..\n \n")



menu()
