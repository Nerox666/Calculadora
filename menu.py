def menu():
    os.system("cls")
    print("****************************************************")
    print("*******************Bienvenido***********************")
    print("****************************************************")
    print("**********Seleccione operacion a realizar***********")
    print("****************************************************")
    print("1. Multiplicar normal")
    print("2. Multiplicación de varias tablas")
    print("3. Puntuaciones")
    print("4. Salir")

    print("Elige la operación")

    try:
        op = int(input('Selecciona una opcion'))
        if(not op <= 4 and not op >= 1):
            print('No es valido introduce de nuevo.')
            input()
        else:
            return op
    except ValueError:
        print('Introduce un número')
