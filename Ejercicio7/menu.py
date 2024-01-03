import os
menu = "1. Registrar productos\n2. Visualizar Inventario\n3. Actualizar Stock\n4. Informe Productos criticos\n5. Ganancia Potencial\n6. Salir"

def menuPpal()->int:
    hasError = True
    print(menu)
    while (hasError):
        try:
            return int(input(":)"))
        except ValueError:
            print("Error en el dato de de ingreso")
            os.system("pause")            
            hasError = True

