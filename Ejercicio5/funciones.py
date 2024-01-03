import os
sismos = []

def regCiudad():
    os.system("cls")
    global sismos
    print("Solo puede registrar 5 ciudades")
    for i in range (0,5):
        nombre=input(f"Ingrese la ciudad numero {i+1}: ")
        ciudad=[nombre,[]]
        sismos.append(ciudad)
    print("Finalizo el registro de la ciudad, seleccione una nueva opcion")
    os.system("pause")

def regSismo():
    os.system("cls")
    global sismos
    print("Ingrese los movimientos teluricos para cada una de las ciudades registradas\n")
    for i in range (0,5):
        isInt=True
        while isInt:
            try:
                sismos[i][1].append(float(input(f"Ingrese el sismo presentado en la ciudad de {sismos[i][0]}: ")))
                isInt=False
            except ValueError:
                print("Olvido ingresar un valor")
                
def buscar():
    print("Ciudades registradas")
    i=0
    for item in sismos:
        print(f"{i+1}. {item[0]}")
        i+=1
    indice = int(input("Seleccione la ciudad de la cual quiera ver los sismos presentados: "))-1
    for i in range(len(sismos[indice][1])):
        print(f"{i+1}. Sismo: {sismos[indice][1][i-1]}")

def informe():
    global sismos
    os.system("cls")
    for item in range(len(sismos)):
        suma = 0
        promedio = 0
        for i in range(len(sismos[item][1])):
            suma = suma + sismos[item][1][i]
        promedio = round(suma/len(sismos[item][1]),1)
        if promedio<=2.5:
            print(f"La ciudad {sismos[item][0]} se encuentra en riesgo Amarillo (Sin riesgo) con un promedio de {promedio}")
        elif 2.6<promedio<=4.5:
            print(f"La ciudad {sismos[item][0]} se encuentra en riesgo Naranja (Riesgo medio) con un promedio de {promedio}")
        else:
            print(f"La ciudad {sismos[item][0]} se encuentra en riesgo Rojo (Riesgo alto) con un promedio de {promedio}")
            


