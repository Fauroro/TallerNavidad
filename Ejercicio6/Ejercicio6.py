import os
import menu
import funciones
import consumo

isActive = True
dependencia = []

while isActive:
    os.system("cls")
    print("""
    ***********************
    *   Calculo de CO2    *
    ***********************
    """)
    try:
        opMenu = menu.menuPpal()
    except ValueError:
        print("Error en el dato de de ingreso")
        os.system("pause")
    else:
        if opMenu==1:
            rta = "S"
            while rta in ["S","s"]:
                os.system("cls")
                dependencia.append(funciones.registar())
                rta = input("Desea registrar otra dependencia S(si) o N(no): ")
            os.system("pause")
        elif opMenu==2:
            rta = "S"
            while rta in ["S","s"]:
                os.system("cls")
                funciones.consumo(dependencia)
                rta = input("Desea registrar el consumo de otra dependencia S(si) o N(no): ")
            os.system("pause")
        elif opMenu==3:
            consumo.produccion(dependencia)
            os.system("pause")
        elif opMenu==4:
            consumo.mayor(dependencia)
            os.system("pause")
        elif opMenu==5:
            isActive = False
        else:
            print("Opcion seleccionada inexistente.")
            os.system("pause")
