import os


PuntuacionVariasTabs = 0
PuntuacionMult  = 0



def resultados(aciertos, errores, nmult):
    print(f'Has tenido {aciertos} aciertos y {errores} errores')

    porcentaje = aciertos/nmult * 100
    print(f"acierto del {porcentaje}" + "%" )
    input()
    porcentaje = round(porcentaje)
    return  porcentaje 
    
 

def mult():
    os.system("cls")

    print("Cual tabla quieres elegir?")
    num1 = int(input("introduce el número "))
   

    return num1







    