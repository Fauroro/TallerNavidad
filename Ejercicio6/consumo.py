import os

def produccion(dependencia:list):
    prodTotal = 0
    for item in range(len(dependencia)):
        prodDepen = 0
        for i in range(len(dependencia[item][1])):
            prodDepen = prodDepen + dependencia[item][1][i]
        print(f"El CO2 producido por la dependencia {dependencia[item][0]} es: {round(prodDepen/1000,2)} kgCO2")
        prodTotal = prodTotal + prodDepen
    print(f"\nEl CO2 producio en total es: {round(prodTotal/1000,2)} kgCO2")

def mayor(dependencia:list):
    mayor = -1
    temp = 0
    for item in range(len(dependencia)):
        prodDepen = 0
        for i in range(len(dependencia[item][1])):
            prodDepen = prodDepen + dependencia[item][1][i]
        if prodDepen>temp:
            temp = prodDepen
            mayor = item
    print(f"\nLa dependencia que mas CO2 produce es {dependencia[mayor][0]} con: {round(temp/1000,2)} kgCO2 producidos\n")
