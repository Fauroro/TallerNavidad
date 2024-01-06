import os
sumNum = 0
cont=0
os.system("cls")
print("El siguiente programa solicitara números enteros positivos e imprimira la sumatoria de los 3 números.\n")
while (cont<3):
    try:
        num = int(input("Ingrese el numero: "))
        if num>0 :
            sumNum=sumNum+num
            cont+=1
        else:
            print("El numero ingresado no es un entero positivo; por favor ingrese otro numero")
    except ValueError:
        print("El numero ingresado no es un entero; por favor ingrese otro numero")

os.system("cls")
print(f"La sumatoria de los numeros ingresados es = {sumNum}")

os.system("pause")