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
    ************************
    *   Categoria -> IMC   *
    ************************
""")
insuf=0
ideal=0
obesidad1=0
obesidad2=0
obesidad3=0
sobrepeso=0
for i in range(20):
    nombre = input("Ingrese el nombre del estudiante: ")
    valor=float()
    edad=validacion(valor,"edad",int)
    peso=validacion(valor,"peso (Kg)",float)
    estatura=validacion(valor,"estatura (m)",float)

    os.system("cls")
    imc=round(peso/(estatura**2),1)
    if (imc<18.5):
        insuf+=1
    elif (imc>=18.5 and imc<24.9):
        ideal+=1
    elif (imc>=25 and imc<29.9):
        sobrepeso+=1
    elif (imc>=30 and imc<34.9):
        obesidad1+=1
    elif (imc>=35 and imc<39.9):
        obesidad2+=1
    else:
        obesidad3+=1

print(f"Numero de estudiantes con peso insuficiente: {insuf}")
print(f"Numero de estudiantes con peso ideal: {ideal}")
print(f"Numero de estudiantes con sobrepeso: {sobrepeso}")
print(f"Numero de estudiantes con obesidad grado 1: {obesidad1}")
print(f"Numero de estudiantes con obesidad grado 2: {obesidad2}")
print(f"Numero de estudiantes con obesidad grado 3: {obesidad3}")