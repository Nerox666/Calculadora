import os
from operaciones import resultados
from puntuacion import guardarpuntuacion
import random as rd


def calculo_varios():
    aciertos = 0
    errores = 0
    nmult = 0

    tabList = None
    while tabList is None:
            try:
                tabList = list(map(int,input("Selecciona tablas (separadas por un espacio) ").split(" ")))
                break           
            except BaseException:
                tabList = None

    isRandom = None
    while  isRandom  is None:
        try:
            isRandom = int(input("Quieres random? 1- si 0- no"))
        except:
            isRandom = None

    for tab in tabList:
        limite = None
        while limite is None:
            try:
                limite = int(input("Cuantas multiplicaciones quieres hacer? "))
            except:
                limite = None
        for i in range(1,limite):
            os.system("CLS") 
            if isRandom:
                num2 = rd.randint(1,10)
            else:
                num2 = i
            solucion = tab * num2
                
            print(f'Cuanto es : {tab} x {num2} ?')
            
            respuesta = None
            while respuesta is None:
                try:
                    respuesta = int(input("Tu respuesta --> "))
                    break
                except ValueError:
                    respuesta = None
                
            if respuesta == solucion:
                print("\nAcertaste\n")
                aciertos = 1 + aciertos
                nmult += 1
            else:
                print(f'\nFallaste, El resultado es: {solucion}\n')
                errores = 1 + errores
                nmult += 1

    result = resultados(aciertos, errores,nmult)

    guardarpuntuacion("Multiplicaciones Varias", result)

def calculo(num1):

    aciertos = 0
    errores = 0

    limite = None
    while limite is None:       
        try:
            limite = int(input("cuantas multiplicaciones quieres hacer?"))  
        except:
            limite = None

    
    isRandom = None
    while isRandom is None:
        try:
            isRandom = int(input("Quieres random? 1- si 0- no"))
        except: 
            isRandom = None

    for i in range(1,limite+1):
            os.system("cls")
            if isRandom:
                num2 = rd.randint(1,10)
            else:
                num2 = i
            print(f'Cuanto es {num1} por {num2}:')

            try:
                resultado = int(input("Selecciona tu respuesta "))
            except ValueError:
                print("el caracter introducido no es válido")
            
            if resultado == num1 * num2:
                print("Has acertado")
                input()
                aciertos = aciertos + 1
            else:
                print(f"fallaste, el número era: {num1 * num2}")
                input()
                errores = errores + 1
    
    result = resultados(aciertos, errores, limite)

    guardarpuntuacion("Multiplicaciones", result)