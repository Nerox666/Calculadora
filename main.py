import os 
from puntuacion import  puntuaciones, leer
from operaciones import mult
from menu import menu
from calc import calculo, calculo_varios

var1 = 0
var2 = 0

# var1,var2 = leer()

print(var1,var2)


def Main():

    opcion = menu()

    if opcion == 1:
       res = mult()
       calculo(res)
    elif opcion == 2:
        calculo_varios()
    elif opcion == 3:
        puntuaciones(var1,var2)
    elif opcion == 4:
        print("hasta luego!!!")
        exit()

Main()

# Pensar en como hacer el menu resistente

# Que hacer si no tengo un fichero creado