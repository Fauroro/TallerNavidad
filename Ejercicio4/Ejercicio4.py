import os
cont=0
num=0
pares=0
impar=0
menor10=0
inter=0
mayor10=0
contImpar=0
contPar=0

os.system("cls")
print("""
    ****************************
    *  Ejercicios con numeros  *
    ****************************
""")
print("""Este programa le permite ingresar n números enteros positivos 
Cuando se ingrese un numero negativo se finalizara la ejecucion y le mostrara el reporte
""")
while (True):
    try:
        num = int(input("Ingrese el numero: "))
        if num>0 :
            if num % 2 == 0:
                pares=pares+num
                contPar+=1
            else:
                impar=impar+num
                contImpar+=1 
            if num<10:
                menor10+=1
            elif num<50 and num>20:
                inter+=1
            elif num>100:
                mayor10+=1       
            cont+=1
    except ValueError:
        print("El numero ingresado no es un entero; por favor ingrese otro numero")
    if num<0:
        break


print(f"La cantidad de numeros ingresados fue: {cont}")
print(f"La cantidad de numeros pares ingresados fue: {contPar}")
print(f"El promedio de los numeros pares es: {round(pares/contPar,2)}")
print(f"El promedio de los numeros impares es: {round(impar/contImpar,2)}")
print(f"La cantidad de numeros menores que 10 fue: {menor10}")
print(f"La cantidad de numeros entre 20 y 50: {inter}")
print(f"La cantidad de numeros mayores que 100 fue: {mayor10}")

