import os

#-.-.-VARIABLES-.-.-

opcion_menu=""
patente=""
marca=""
obs=""
nombre_auto=""
fecha=""
op=""
observacion=""
lista_auto=[]
lista_observaciones=[]
lista_patente=[]
lista_marca=[]
lista_tipo=[]
lista_año=[]
modelo=0
año_fabricacion=0
tipo_vehiculo=""
registros=""

#-.-.-.-Codigo pricipal-.-.-.-

while True:
    os.system("cls")
    opcion_menu=str(input('''
            -.-.-MENÚ-.-.-
            1.- Registrar automovil
            2.- Registro Mantenimiento
            3.- Consultar Automovil
            4.- Salir
            Elija opcion:      '''))
    if opcion_menu == "1":
        os.system ("cls")
        print("\n-.-.-.-Ingrese patente-.-.-")
        patente=str(input("Ingrese patente:   ")).strip().upper()
        while not len (patente) ==6:
            print("Error... debe tener 6 caractéres!!")
            patente=str(input("Ingrese patente:   ")).strip().upper()
        lista_patente.append(patente)
        
        nombre_auto=str(input("ingrese nombre:   ")).strip().upper()
        while not len(nombre_auto)>0:
            print("Error.. no puede dejar el campo vacío")
            nombre_auto=str(input("Ingrese nombre")).strip().upper()
        lista_auto.append(modelo)
        
        marca=str(input("Ingrese marca:     ")).strip().upper()
        while not len(marca)>0:
            print("Error.. no puede dejar este campo vacío")
            nombre=str(input("Ingresa marca de vehículo")).strip().upper()
        lista_marca.append(marca)
        
        tipo_vehiculo=str(input("Ingrese tipo de vehículo:  ")).strip().lower()
        while tipo_vehiculo not in ["d", "b", "e", "h", "D", "B", "E", "H"]:
            print("Error... puede ser d/b/e/h mayúscula o minúscula")
            tipo_vehiculo=str(input("Ingrese tipo de vehículo:  "))
        lista_tipo.append(tipo_vehiculo)
        
        año_fabricacion=int(input("Igrese año de fabricación:   "))
        while not 1899< año_fabricacion <=2021:
            print("Error... fuera de rango")
            año_fabricacion=int(input("Ingrese el año, porfavor:    "))
        lista_año.append(año_fabricacion)
        
        
    if opcion_menu == "2":
        os.system("cls")
        print("-.-.-.-.-solicitar patente-.-.-.-")
        for i in range(len(lista_patente)):
            print(f'''
                {lista_patente} {lista_auto[i]}%
                ''')
            os.system("pause")
        
        op=str(input("¿Desea agregar observación? S/N")).strip().upper()
        if op=="S":
            fecha=str(input("Ingrese fecha dd/mm/aaaa:  "))
            observacion=str(input("Ingrese observacion: "))
            obs= f'''
                -.-.-.-.-.-Observación-.-.-.-.-
                Fecha: {fecha}
                Observación: {observacion}
                '''
        else:
            obs="No hay observación"
            lista_observaciones.append(obs)
            os.system("pause")
            
    if opcion_menu == "3":
        os.system("cls")
        print("\n  -.-.-.-.-.-.-Mostrar en pantalla vehículo-.-.-.-.-.-.-")
        print(f'''
            Patente: {patente}
            Módelo: {nombre_auto}
            Tipo de vehículo:  {tipo_vehiculo}
            Año Fabricación: {año_fabricacion}
            Marca: {marca}''')
        os.system("pause")
        
    if opcion_menu == "4":
        print("Cerrando sesión...")
        break