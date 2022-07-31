import os

#------------- VARIABLES -------------

opcion_menu=""  # opción del menú principal

run=""   # Ej. 111-k, NO VACIA!!!!!

lista_runs=[]

nombre=""  # nombre del usuario, no vacia

lista_nombres=[]

edad=0     # edad valor entero entre [18,99]

lista_edades=[]

#------------- CÓDIGO PRINCIPAL -------------

while True:

    os.system("cls")

    opcion_menu=str(input('''

    ---------Menú Principal---------

    1.- Agregar Usuario

    2.- Listar Usuarios

    3.- Buscar Usuario por RUN

    4.- Eliminar un usuario POR RUN

    5.- Modificar un usuario

    6.- Salir                        



    Elije opción:      '''))


    if opcion_menu=="1":

        os.system("cls")

        print("\n----------REGISTRAR USUARIO-------")

        run=str(input("Ingrese run: ")).strip()

        while not len(run)>0:

            print("Error...no se permite cadena vacia")

            run=str(input("Ingrese run: ")).strip()

        lista_runs.append(run)


        nombre=str(input("Ingrese nombre: ")).strip()

        while not len(nombre)>0:

            print("Error...no se permite cadena vacia")

            nombre=str(input("Ingrese nombre: ")).strip()

        lista_nombres.append(nombre)    



        while True:

            try:

                edad=int(input("Ingrese edad: [18-99]  "))

                break

            except ValueError:

                print("Ooops!! debe ser número")                        



        while not 18<=edad<=99:

            print("Error..fuera de rango [18-99]")

            edad=int(input("Ingrese edad: [18-99]  "))

        lista_edades.append(edad)    



        print(f'''

                {lista_runs}

                {lista_nombres}

                {lista_edades}   ''')  


        os.system("pause")



    if opcion_menu=="2":

        os.system("cls")

        print("\n---------LISTAR USUARIOS--------")

        print("\nRUN \t NOMBRE \t EDAD")

        for k in range(len(lista_runs)):

            print(f'''

{lista_runs[k]} \t {lista_nombres[k]} \t\t {lista_edades[k]}      

                    ''')



        os.system("pause")

    if opcion_menu=="3":

        os.system("cls")

        print("\n-----------BUSCAR UN REGISTRO----------")

        run= str(input("Ingrese run a buscar: ")).strip()

        while not len(run)>0:

            print("Error...no se permite cadena vacia")

            run=str(input("Ingrese run: ")).strip()

        # Si el RUN esta CONTENIDO DENTRO DE lista_runs

        if (run in lista_runs):

            # retorna la posición(indice) del registro

            # que coincide con el RUN

            k= lista_runs.index(run)

            print(f'''\n Nombre:{lista_nombres[k]} \t Edad:{lista_edades[k]}      ''')

        else:

            print("\n EL RUN no esta en la BD")    



        os.system("pause")



    if opcion_menu=="6":

        op=str(input("¿Estas seguro de salir? S/N ")).upper()

        if op=="S":

            break
