import os
txtCat = "1. Novato (edad entre 15 y 16 años)\n2. Intermedio (edad entre 17 y 20 años)\n3. Avanzado (edad mayores a 20 años)\n4. Cancelar"

def subReg(men,may,id):
    print("\nRecuerde que no puede comenzar la categoria sin inscribir por lo menos a 5 jugadores.\n")
    edad = int(input("Ingrese la edad del jugador que va a inscribir: "))
    if men<=edad<=may:
        nombre = input("Ingrese el nombre del jugador: ")
        id+=1
        print(f"\n El ID unico para el jugador que acaba de inscribir es {id}\n")
        jugador={
            "nombre":nombre,
            "edad":edad,
            "puntuacion":{
                "pj":0,
                "pg":0,
                "pp":0,
                "pa":0,
                "tp":0
            }
        }
        os.system("pause")
        return{id:jugador}
    else:
        print("El jugador no pertenece a esta categoria porque no cumple con la edad")
        os.system("pause")
        return {}


idNov = 100
idInte = 300
idAva = 500
novato = {}
intermedio = {}
avanzado = {}
def registrar():
    global idNov,idInte,idAva
    os.system("cls")
    print(f"Jugadores inscritos:\nNovato: {len(novato)}\t\tIntermedio: {len(intermedio)}\t\tAvanzado: {len(avanzado)}")
    print(f"Seleccione la categoria de la cual quiere inscribir a un jugador:\n{txtCat}")
    opCat = int(input(":) "))
    if opCat==1:
        novato.update(subReg(men=15,may=16,id=idNov))
        idNov+=1
        return {"novato":novato}
    elif opCat==2:
        intermedio.update(subReg(men=17,may=20,id=idInte))
        idInte+=1
        return{"intermedio":intermedio}
    elif opCat==3:
        avanzado.update(subReg(men=21,may=100,id=idAva))
        idAva+=1
        return{"avanzado":avanzado}
    elif opCat==4:
        return{}
    else:
        print("Opcion seleccionada inexstente.")
    
