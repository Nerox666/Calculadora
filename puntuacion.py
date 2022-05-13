import json
import os
from menu import menu

def leer():
    
    PuntuacionVariasTabs = 0
    PuntuacionMult  = 0
    with open("puntuaciones.json", "r") as f:
        _dict:dict = json.load(f)
    
    for t, valor in _dict.items():
        if t == "Multiplicaciones Varias":
            PuntuacionVariasTabs = valor
        else:
            PuntuacionMult  = valor
            
    return PuntuacionMult,PuntuacionVariasTabs

def guardarpuntuacion(nombrecampo, porcentaje):
    
    
    _dict = {}
    
    with open ("puntuaciones.json", "r") as f:
        _dict = json.load(f)

    with open("puntuaciones.json", "w+") as f:
        _dict[nombrecampo] = porcentaje
        f.write(json.dumps(_dict))



def puntuaciones(PuntuacionMult,PuntuacionVariasTabs):




    os.system("cls")
    print("*******************Resultados**********************")
    print("***************************************************")
    print("*****(es la diferencia entre errores y aciertos)***")
    print("---------------------------------------------------")
    print(f"| conocimiento multiplicaciones:    {PuntuacionMult}% |")
    print(f"| conocimiento varias tablas: {PuntuacionVariasTabs}% |")
    print("---------------------------------------------------")


    op = input("pulsa r para salir y volver al menú")
    if op.lower() == "r" or op.upper() == "R":
        menu()
