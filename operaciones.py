from cgi import print_directory
from distutils.log import error
import os
import random as rd
import json




PuntuacionVariasTabs = 0
PuntuacionMult  = 0


    

def resultados(aciertos, errores):
    print(f'Has tenido {aciertos} aciertos y {errores} errores')

    porcentaje = aciertos/10 * 100
    print(f"acierto del {porcentaje} " + "%" )
    input()
    menu()
 
   


def mult():
    os.system("cls")

    print("Cual tabla quieres elegir?")
    num1 = int(input("introduce el número "))
   

    print('Quieres de forma desordenada? (S/n/N/n) ')

    respuesta = input()

    if respuesta.upper() == "S"  or respuesta.lower() == "s":
        num2 = rd.randint(1,10)
    elif respuesta.upper() == "N"  or respuesta.lower() == "n":
        num2 = 1

    calculo(num1, num2, "Multiplicaciones ordenadas")

    os.system("cls")

def multvarios():

    aciertos = 0
    errores = 0

    contador = 0
    while True:
            try:
                info = input("Selecciona tablas (separadas por un espacio) ")
                break           
            except ValueError:
                os.system("CLS")
                print("Selecciona tablas (separadas por un espacio) \n")

    while True:
            try:
                tab = list(map(int,info.split(" ")))
                break           
            except BaseException:
                multvarios()
        
    contadorTablas = len(tab)        
    pos = 0
    os.system("CLS")    
        
    calculo_varios(aciertos, errores, contador,contadorTablas, pos, tab,"Multiplicaciones Varias")


def multvariosrand():
    aciertos = 0
    errores = 0

    contador = 0
    while True:
            try:
                info = input("Selecciona tablas (separadas por un espacio) ")
                break           
            except ValueError:
                os.system("CLS")
                print("Selecciona tablas (separadas por un espacio) ")

    while True:
            try:
                tab = list(map(int,info.split(" ")))
                break           
            except BaseException:
                multvarios()
        
    contadorTablas = len(tab)        
    pos = 0
    os.system("CLS")    
        
    while (pos < contadorTablas):
        while (contador < 11):

            num2 = rd.randint(1,10)
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
            contador = contador + 1
            
            
        contador = 0

        pos = 1 + pos

    resultados(aciertos, errores)


     



menu()
