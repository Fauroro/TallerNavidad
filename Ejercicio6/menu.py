import os
menu = "1. Registrar Dependencia\n2. Registrar consumo por dependencia\n3. Ver CO2 producido\n4. Dependencia que produce mayor CO2\n5. Salir"

def menuPpal()->int:
    print(menu)
    hasError = True
    while (hasError):
        try:
            return int(input(":)"))
        except ValueError:
            print("Error en el dato de de ingreso")
            os.system("pause")            
            hasError = True