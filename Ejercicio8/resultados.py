import os

def puntuacion(torneo:dict):
    # print(torneo.get("novato"))
    os.system("cls")
    print("Jugadores inscritos:")
    for x in torneo:
        print(f"{x}: {len(torneo[x])}",end="\t\t")
    num=0
    print("\nSeleccione la categoria que registrara resultados: ")
    for x in torneo:
        num+=1
        print(f"{num}. {x}")
    print("4. Cancelar")
    isActive = True
    setP1,setP2,puntos1,puntos2 = 0
    while isActive:
        try:
            cat = int(input(":) "))
        except ValueError:
            print("Error en el dato de ingreso, intente nuevamente")
            os.system("pause")
        else:
            if cat==1:
                if len(torneo["novato"])<2:
                    print(f"No es posible iniciar los juegos en la categoria seleccionada por falta de participantes, faltan {5-len(torneo['novato'])} jugadores ")
                    os.system("pause")
                    isActive = False
                else:
                    novato = torneo.get("novato")
                    sets=input("Digite la cantidad de sets que se jugaron en el partido: ")
                    print("JUgadores de la Categoria:")
                    for x,y in novato.items():
                        print(f"{x} {y['nombre']}")
                    p1 = int(input("Ingrese el ID del jugador A: "))
                    novato[f'{p1}']['puntuacion'].update({'pj':pj+1})
                    p2 = int(input("Ingrese el ID del jugador B: "))
                    novato[f'{p2}']['puntuacion'].update({'pj':pj+1})

                    for i in range(1,sets):
                        marc1 = int(input("Ingrese el marcador para el jugador A: "))
                        marc2 = int(input("Ingrese el marcador para el jugador B: "))
                        if marc1<marc2:
                            setP2 +=1
                            puntos2 = marc2 - marc1
                        elif marc2<marc1:
                            setP1 +=1
                            puntos1 = marc1 - marc2
                            
                    # if setP2<setP1:

                    for x,y in novato.items():
                        if p1==x:
                            temp = y['puntuacion']['pj']
                            pj = temp + 1
                            y['puntuacion'].update({'pj':pj})
                        if p2==x:
                            temp = y['puntuacion']['pj']
                            pj = temp + 1
                            y['puntuacion'].update({'pj':pj})
                    print(f'nov {novato}')
                    torneo.update({'novato':novato})
                    print(f'tro {torneo}')
                    marc1 = int(input("Ingrese el marcador para el jugador: "))
    

                    return {'novato':novato}
                    os.system("pause")
            elif cat==2:
                os.system("pause")
            elif cat==3:
                os.system("pause")
            elif cat==4:
                isActive = False
            else:
                print("Opcion seleccionada inexistente.")
                os.system("pause")
                isActive = True


