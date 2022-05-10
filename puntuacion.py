
def guardarpuntuacion(aciertos, errores, nombrecampo, nombrepuntuacion):
   json = ""
   with open("puntuaciones.json" , "w") as fichero:
         json = json.load(fichero)
   
   nombrepuntuacion
   nombrepuntuacion = aciertos - errores
   json[nombrecampo] = nombrepuntuacion



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
