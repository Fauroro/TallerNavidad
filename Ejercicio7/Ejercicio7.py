import os
import menu
import funciones
invent = []
isActive = True

while isActive:
    os.system("cls")
    print("""
    *******************************
    *   Gestion de inventarios    *
    *******************************
    """)
    try:
        opMenu = menu.menuPpal()
    except ValueError:
        print("Error en el dato de de ingreso")
        os.system("pause")
    else:
        if (opMenu==1):
            rta = "S"
            while (rta in ["S","s"]):
                os.system("cls")
                invent.append(funciones.registrar())
                rta = input("Desea registrar otro producto S(si) o N(No)")
        elif (opMenu==2):
            funciones.ver(invent)
            os.system("pause")
        elif (opMenu==3):
            rta = "S"
            while (rta in ["S","s"]):
                os.system("cls")
                funciones.actStock(invent)
                rta = input("Desea actualizar otro producto S(si) o N(No)")            
            os.system("pause")
        elif (opMenu==4):
            funciones.informe(invent)
            os.system("pause")
        elif (opMenu==5):
            funciones.ganancia(invent)
            os.system("pause")
        elif (opMenu==6):
            isActive=False
        else:
            print("Opcion seleccionada inexistente.")
            os.system("pause")


