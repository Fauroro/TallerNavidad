import os
def validacion(valor,txt,tipo):
    valor=0
    while (valor<=0):
        try:
            valor = tipo(input(f"Ingrese {txt} del estudiante: "))
        except ValueError:
            print("Error en el dato de ingreso, intente otra vez")
            os.system("pause")
        else:
            if valor<=0:
                print("Error en el dato de ingreso, intente otra vez")    
    return valor

os.system("cls")
print("""
    **********************************
    * Indice de masa corporal -> IMC *
    **********************************
""")
nombre = input("Ingrese el nombre del estudiante: ")

valor=float()
edad=validacion(valor,"edad",int)
peso=validacion(valor,"peso (Kg)",float)
estatura=validacion(valor,"estatura (m)",float)

os.system("cls")
print("Nombre\tEdad\tIMC\tCategoria")
imc=round(peso/(estatura**2),1)
if (imc<18.5):
    print(f"{nombre}\t{edad}\t{imc}\tInsuficiente")
elif (imc>=18.5 and imc<24.9):
    print(f"{nombre}\t{edad}\t{imc}\tNormal")
elif (imc>=25 and imc<29.9):
    print(f"{nombre}\t{edad}\t{imc}\tSobrepeso")    
elif (imc>=30 and imc<34.9):
    print(f"{nombre}\t{edad}\t{imc}\tObesidad I")
elif (imc>=35 and imc<39.9):
    print(f"{nombre}\t{edad}\t{imc}\tObesidad II")
else:
    print(f"{nombre}\t{edad}\t{imc}\tObesidad III")

