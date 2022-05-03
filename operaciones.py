from cgi import print_directory
from distutils.log import error
import os
from pprint import pprint
import random as rd
import math as mt
from time import process_time_ns
import json

from numpy import False_ 


PuntuacionVariasTabsOrdenadas  = 0
PuntuacionVariasTabsDesOrdenadas  = 0
PuntuacionMult  = 0

def menu():
    os.system("cls")
    print("****************************************************")
    print("*******************Bienvenido***********************")
    print("****************************************************")
    print("**********Seleccione operacion a realizar***********")
    print("****************************************************")
    print("1. Multiplicar normal")
    print("2. Multiplicación de varias tablas de forma ordenada")
    print("3. Multiplicación de varias tablas de forma desordenada")
    print("4. Puntuaciones")
    print("5. Salir")

    print("Elige la operación")

    try:
        op = int(input())
    except:
        print("introduce una operacion válida")

    if op == 1:
        mult()
    elif op == 2:
        multvarios()
    elif op == 3:
        multvariosrand()
    elif op == 4:
        puntuaciones()   
    elif op == 5:
        print("Hasta luego !!")
        exit()
    

def resultados(aciertos, errores):
    print(f'Has tenido {aciertos} aciertos y {errores} errores')

    porcentaje = aciertos/10 * 100
    print(f"acierto del {porcentaje} " + "%" )
    input()
    menu()

   
def guardarpuntuacion(aciertos, errores, nombrecampo, nombrepuntuacion):
   json = ""
   with open("puntuaciones.json" , "w") as fichero:
         json = json.load(fichero)
   
   nombrepuntuacion
   nombrepuntuacion = aciertos - errores
   json[nombrecampo] = nombrepuntuacion

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

    br = 0
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
        
    cont = len(tab)        
    pos = 0
    os.system("CLS")    
        
    while (pos < cont):
        while (br < 11):

            num2 = br
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
                
            br = 1 + br
            

        br = 0
            
        pos = 1 + pos

    resultados(aciertos, errores)

    menu()

    
    

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


     

def puntuaciones():

    valoracionmultord = ""
    valoracionmultrand = ""
    valoracionvariasmultord = ""
    valoracionvariasmultrand = ""

    
    if PuntuacionMultOrdenadas <= 4  :
        valoracionmultord = "Insuficiente, necesita practicar mucho" 
    elif PuntuacionMultOrdenadas >= 8 :
        valoracionmultord = " Bastante bien un poco mas y lo saca"
    elif PuntuacionMultOrdenadas == 10 :
        valoracionmultord = "Ha completado todo"
    else:
        valoracionmultord = "bien, sigue así"

    if PuntuacionMultDesOrdenadas <= 4  :
        valoracionmultrand = "Insuficiente, necesita practicar mucho" 
    elif PuntuacionMultDesOrdenadas >= 8 :
        valoracionmultrand = " Bastante bien un poco mas y lo saca"
    elif PuntuacionMultDesOrdenadas == 10 :
        valoracionmultrand = "Ha completado todo"
    else:
        valoracionmultrand = "bien, sigue así"


    if PuntuacionVariasTabsOrdenadas <= 4  :
        valoracionvariasmultord = "Insuficiente, necesita practicar mucho" 
    elif PuntuacionVariasTabsOrdenadas >= 8 :
        valoracionvariasmultord = " Bastante bien un poco mas y lo saca"
    elif PuntuacionVariasTabsOrdenadas == 10 :
        valoracionvariasmultord = "Ha completado todo"
    else:
        valoracionvariasmultord = "bien, sigue así"

    
    if PuntuacionVariasTabsDesOrdenadas <= 4  :
        valoracionvariasmultrand = "Insuficiente, necesita practicar mucho" 
    elif PuntuacionVariasTabsDesOrdenadas >= 8 :
        valoracionvariasmultrand = " Bastante bien un poco mas y lo saca"
    elif PuntuacionVariasTabsDesOrdenadas == 10 :
        valoracionvariasmultrand = "Ha completado todo"
    else:
        valoracionvariasmultrand = "bien, sigue así"


    os.system("cls")
    print("*******************Resultados**********************")
    print("***************************************************")
    print("*****(es la diferencia entre errores y aciertos)***")
    print("---------------------------------------------------")
    print(f"| conocimiento multiplicaciones ordenadas:    {PuntuacionMultOrdenadas} |")
    print(f"| conocimiento multiplicaciones desordenadas: {PuntuacionMultDesOrdenadas} |")
    print(f"| conocimiento varias tablas ordenadas: {PuntuacionVariasTabsOrdenadas}       |")
    print(f"| conocimiento varias tablas desordenadas: {PuntuacionMultDesOrdenadas}    |")
    print("---------------------------------------------------")
    print("*******************Valoraciones********************")
    print("----------------------------------------------------------------------------")
    print(f"| conocimiento multiplicaciones ordenadas: {valoracionmultord} |")
    print(f"| conocimiento multiplicaciones desordenadas: {valoracionmultrand} |")
    print(f"| conocimiento varias tablas ordenadas: {valoracionvariasmultord}       |")
    print(f"| conocimiento varias tablas desordenadas: {valoracionvariasmultrand}    |")
    print("-----------------------------------------------------------------------------")


    op = input("pulsa r para salir y volver al menú")
    if op.lower() == "r" or op.upper() == "R":
        menu()


menu()
