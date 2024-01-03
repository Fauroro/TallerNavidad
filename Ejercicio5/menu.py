import os
menu = "1. Registrar Ciudad\n2. Registrar Sismo\n3. Buscar sismos por ciudad\n4. Informe de riesgo\n5. Salir"

def menuPpal() -> int:
    hasError = True
    print(menu)
    while (hasError):
        try:
            return int(input(":)"))
        except ValueError:
            print("Error en el dato de de ingreso")
            os.system("pause")            
            hasError = True
