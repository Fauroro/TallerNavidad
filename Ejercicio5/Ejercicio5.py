import os
import menu
import funciones

isActive = True
opMenu=0

while (isActive) :
    os.system("cls")
    print("""
    **********************************
    * Centro de prevencion de Sismos *
    **********************************
    """)
    try:
        opMenu = menu.menuPpal()
    except ValueError:
        print("Error en el dato de de ingreso")
        os.system("pause")
    else:
        if(opMenu == 1):
            funciones.regCiudad()
        elif (opMenu == 2):
            rta = "S"
            while (rta in ["S","s"]):
                os.system("cls")
                funciones.regSismo()
                rta = input("Desea registrar otro sismo S(si) o N(No)")        
            os.system("pause")
        elif (opMenu == 3):
            rta = "S"
            while (rta in ["S","s"]):
                os.system("cls")
                funciones.buscar()
                rta = input("Desea buscar otra ciudad S(si) o N(No)")        
            os.system("pause")
        elif (opMenu == 4):
            funciones.informe()
            os.system("pause")
        elif (opMenu == 5):
            isActive = False  
        else:
            print("Ingrese una opcion valida.") 
            os.system("pause")     
            