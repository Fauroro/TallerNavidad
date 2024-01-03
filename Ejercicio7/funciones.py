import os
producto = []
valor=0
inventario = ["Codigo","Nommbre del producto","Valor de compra","Valor de venta","Stock Minimo", "Stock Maximo","Proveedor"]
def valid(valor,txt,tipo):
    valor=0
    while (valor<=0):
        try:
            valor = tipo(input(txt))
        except ValueError:
            print("Error en el dato de ingreso, intente otra vez")
        else:
            if valor<=0:
                print("Error en el dato de ingreso, intente otra vez")    
    return valor

def registrar()->list:
    global valor
    codigo = input("Ingrese el codigo del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    compra = valid(valor,"Ingrese el valor de compra del producto: ",float)
    venta = valid(valor,"Ingrese el valor de venta del producto: ",float)
    sMin = valid(valor,"Ingrese en Stock Minimo permitido del producto: ",int)
    sMax = valid(valor,"Ingrese en Stock Maximo permitido del producto: ",int)
    proveedor = input("Ingrese el nombre del proveedor del producto: ")
    producto = [codigo,nombre,compra,venta,sMin,sMax,proveedor]
    return (producto)

def ver(invent:list):
    os.system("cls")
    global inventario
    print("\tINVENTARIO")
    for i in range(len(invent)):
        for j in range(len(invent[i])):
            print(f"{inventario[j]}: {invent[i][j]}")
        print("-------------------------------------------------------")

def actStock(invent:list):
    tempCod=input("Digite el codigo del producto del cual desea actualizar el inventario: ")
    for item in invent:
        if tempCod in item:
            indice = invent.index(item)
            print(f"Codigo: {invent[indice][0]}\nNombre: {invent[indice][1]}\nStock actual: {invent[indice][5]}")
    isActive = True
    while isActive:
        try:
            select=int(input("\nSeleccione la opcion para lo que desea hacer con el stock del producto:\n1. Agregar\n2. Disminuir\n3. Cancelar\n:)"))
        except ValueError:
            print("Error en el dato de ingreso, intente otra vez")
        else:
            if select==1:
                tempModif = int(input("Ingrese la cantidad a adicionar: "))
                invent[indice][5]=invent[indice][5] + tempModif
                isActive = False
            elif select==2:
                tempModif = int(input("Ingrese la cantidad a disminuir: "))
                invent[indice][5]=invent[indice][5]-tempModif
                isActive = False
            elif select==3:
                isActive = False
            else:
                print("Seleccione una opcion existente")
                isActive = True
    print(f"\nCodigo: {invent[indice][0]}\nNombre: {invent[indice][1]}\nStock actual: {invent[indice][5]}")

def informe(invent:list):
    os.system("cls")
    global inventario
    print("Productos con un Stock menor al permitido: ")
    for i in range(len(invent)):
        for j in range(len(invent[i])):
            if invent[i][5]<invent[i][4]:
                print(f"{inventario[j]}: {invent[i][j]}")
        print("-------------------------------------------------------")

def ganancia(invent:list):
    os.system("cls")
    gan = 0
    for i in range(len(invent)):
        gan = gan + (invent[i][3]-invent[i][2])*invent[i][5]
    print(f"La Ganancia Potencial Total es igual a: ${gan}")
