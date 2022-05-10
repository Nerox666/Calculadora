def calculo_varios(aciertos, errores, contador,contadorTablas, pos, tab, nombrepuntuacion):
    
    print("Quieres de forma aleatoria ? (s/S/N/n)")
    respuesta = input()
    
    if respuesta.upper() == "S"  or respuesta.lower() == "s":
        num2elegidorandom = true
    elif respuesta.upper() == "N"  or respuesta.lower() == "n":
        num2elegidorandom = false

    while (pos < contadorTablas):
        while (contador < 11):

            if num2elegidorandom == true:
                 num2 = rd.randint(1,10)
            elif num2elegidorandom == false:
                 num2 = contador

            num1 = tab[pos]
            solucion = num1 * num2
                
            print(f'Cuanto es : {num1} x {num2} ?')
                
            while True:
                try:
                    respuesta = int(input("Tu respuesta --> "))
                    break
                except ValueError:
                    print("\nSolo se admiten numeros\n")
                    print("Pulsa Enter para volver")
                    input()
                    os.system("CLS")
                    print(f'Cuanto es : {num1} x {num2} ?\n')
                
            if respuesta == solucion:
                print("\nAcertaste\n")
                aciertos = 1 + aciertos
            else:
                print(f'\nFallaste, El resultado es: {solucion}\n')
                errores = 1 + errores
                
            contador = 1 + contador
            

        contador = 0
            
        pos = 1 + pos

    resultados(aciertos, errores)
    # guardarpuntuacion(aciertos, errores, nombrepuntuacion, PuntuacionMultOrdenadas )



def calculo(num1, num2, nombrepuntuacion):

    contador = 0
    aciertos = 0
    errores = 0

    limite = int(input("cuantas multiplicaciones quieres hacer?"))

    while contador != limite:
            os.system("cls")
            print(f'Cuanto es {num1} por {num2}:')

            try:
                resultado = int(input("Selecciona tu respuesta "))
            except ValueError:
                print("el caracter introducido no es válido")
            
            if resultado == num1 * num2:
                print("Has acertado")
                input()
                aciertos = aciertos + 1
            elif resultado != num1 * num2:
                print(f"fallaste, el número era: {num1 * num2}")
                input()
                errores = errores + 1
            contador = contador + 1
            num2 = num2 + 1

   # guardarpuntuacion(aciertos, errores, nombrepuntuacion, PuntuacionMultOrdenadas )
    
    resultados(aciertos, errores)