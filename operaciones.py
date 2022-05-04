from cgi import print_directory
from distutils.log import error
import os
from pprint import pprint
import random as rd
import math as mt
from time import process_time_ns
import json

from numpy import False_
from sqlalchemy import false, true 


PuntuacionVariasTabs = 0
PuntuacionMult  = 0

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
        op = int(input())
    except:
        print("introduce una operacion válida")

    if op == 1:
        mult()
    elif op == 2:
        multvarios()
    elif op == 3:
        puntuaciones()   
    elif op == 4:
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


     

def puntuaciones():

    valoracionmult = ""
    valoracionvariasmult= ""

    
    if PuntuacionMult <= 4  :
         valoracionmult = "Insuficiente, necesita practicar mucho" 
    elif PuntuacionMult >= 8 :
         valoracionmult = " Bastante bien un poco mas y lo saca"
    elif PuntuacionMult == 10 :
         valoracionmult = "Ha completado todo"
    else:
         valoracionmult = "bien, sigue así"
    
    if PuntuacionVariasTabs <= 4  :
        valoracionvariasmult = "Insuficiente, necesita practicar mucho" 
    elif PuntuacionVariasTabs >= 8 :
        valoracionvariasmult = " Bastante bien un poco mas y lo saca"
    elif PuntuacionVariasTabs == 10 :
        valoracionvariasmult = "Ha completado todo"
    else:
        valoracionvariasmult = "bien, sigue así"


    os.system("cls")
    print("*******************Resultados**********************")
    print("***************************************************")
    print("*****(es la diferencia entre errores y aciertos)***")
    print("---------------------------------------------------")
    print(f"| conocimiento multiplicaciones:    {PuntuacionMult} |")
    print(f"| conocimiento varias tablas: {PuntuacionVariasTabs}|")
    print("---------------------------------------------------")
    print("*******************Valoraciones********************")
    print("----------------------------------------------------------------------------")
    print(f"| conocimiento multiplicaciones: {valoracionmult} |")
    print(f"| conocimiento varias tablas: {valoracionvariasmult}       |")
    print("-----------------------------------------------------------------------------")


    op = input("pulsa r para salir y volver al menú")
    if op.lower() == "r" or op.upper() == "R":
        menu()


menu()
