import os
depend = []
def registar():
    global depend
    nombre = input("Ingrese el nombre de la dependencia: ")
    depend = [nombre,[]]
    return depend

def consumo(dependencia:list):
    factor = 164.38
    indice = -1
    print("Las dependencias registradas son:")
    for item in dependencia:
        print(f"* {item[0]}")
    dep = str(input("Escriba el nombre (exactamente como aparece en el anterior listado) de la dependencia de la cual quiere registrar el consumo: "))
    for item in dependencia:
        if dep in item:
            indice = dependencia.index(item)
    if indice==-1:
        print("Dependencia no encontrada, intente nuevamente")
        return
    isActive = True
    while isActive:
        co2=0
        try:
            opCons = int(input("Seleccione la opcion para su caso\n1. Conoce el consumo mensual de la dependencia (Kwh al mes)\n2. Conoce potencia nominal de cada dispositivo (Watts)\n3. Cancelar\n:)"))
        except ValueError:
            print("Error en el dato de ingreso")
        else:
            if opCons==1:
                consumo = float(input("Ingrese el valor consumo electrico de la dependencia en Kwh al mes: "))
                co2 = consumo*factor                
                isActive = False
            elif opCons==2:
                isActivedispo = True
                while isActivedispo:
                    consumo = float(input("Ingrese la potencia nominal en Watts del dispositivo: "))
                    tiempo = float(input("Ingrese las horas aproximadas que dura encendido el dispositivo al dia: "))
                    co2 = co2 + ((consumo*tiempo*30)/1000)*factor
                    rta = input(f"Desea registrar otro dispositivo en la dependencia {dependencia[indice][0]} S(si) o N(no): ")
                    isActive = False
                    if rta in ["s","S"]:
                        isActivedispo = True
                    else:
                        isActivedispo = False
            elif opCons == 3:
                isActive = False                    
            else:
                print("Ingrese una opcion existente")
                isActive == True
            dependencia[indice][1].append(co2)
    #print(dependencia)

