import os
def winSet(cat:dict,jug,puntos1,jugp,puntos2):
    pg = cat[jug]['puntuacion']['pg'] + 1
    cat[jug]['puntuacion'].update({'pg':pg})
    pa = cat[jug]['puntuacion']['pg'] + puntos1
    cat[jug]['puntuacion'].update({'pa':pa})
    pa = cat[jugp]['puntuacion']['pg'] + puntos2
    cat[jugp]['puntuacion'].update({'pa':pa})
    pp = cat[jugp]['puntuacion']['pg'] + 1
    cat[jugp]['puntuacion'].update({'pp':pp})
    tp = cat[jug]['puntuacion']['pg'] + 1
    cat[jug]['puntuacion'].update({'pp':tp})


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
    setP1=0
    setP2=0
    puntos1=0
    puntos2 = 0
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
                    sets=int(input("Digite la cantidad de sets que se jugaron en el partido: "))
                    print("Jugadores de la Categoria:")
                    for x,y in novato.items():
                        print(f"{x} : {y['nombre']}")
                    p1 = int(input("Ingrese el ID del jugador A: "))
                    pj = novato[p1]['puntuacion']['pj'] + 1
                    novato[p1]['puntuacion'].update({'pj':pj})
                    p2 = int(input("Ingrese el ID del jugador B: "))
                    pj = novato[p2]['puntuacion']['pj'] + 1
                    novato[p2]['puntuacion'].update({'pj':pj})

                    for i in range(1,sets+1):
                        marc1 = int(input("Ingrese el marcador para el jugador A: "))
                        marc2 = int(input("Ingrese el marcador para el jugador B: "))
                        if marc1<marc2:
                            setP2 +=1
                            puntos1 = puntos1 + marc1 - marc2
                            puntos2 = puntos2 + marc2 - marc1
                            print(f"Ganador del set {i}: {novato[p2]['nombre']}")
                        elif marc2<marc1:
                            setP1 +=1
                            puntos1 = puntos1 + marc1 - marc2
                            puntos2 = puntos2 + marc2 - marc1
                            print(f"Ganador del set {i}: {novato[p1]['nombre']}")
                            
                    if setP2<setP1:
                        winSet(novato,p1,puntos1,p2,puntos2)
                        # pg = novato[f'{p1}']['puntuacion']['pg'] + 1
                        # novato[f'{p1}']['puntuacion'].update({'pg':pg})
                        # pa = novato[f'{p1}']['puntuacion']['pg'] + puntos1
                        # novato[f'{p1}']['puntuacion'].update({'pa':pa})
                        # pp = novato[f'{p1}']['puntuacion']['pg'] + 1
                        # novato[f'{p1}']['puntuacion'].update({'pp':pp})
                        # tp = novato[f'{p1}']['puntuacion']['pg'] + 1
                        # novato[f'{p1}']['puntuacion'].update({'pp':tp})
                        
                    if setP1<setP2:
                        winSet(novato,p2,puntos2,p1,puntos1)
                        # pg = novato[f'{p2}']['puntuacion']['pg'] + 1
                        # novato[f'{p2}']['puntuacion'].update({'pg':pg})
                        # pa = novato[f'{p2}']['puntuacion']['pg'] + puntos1
                        # novato[f'{p2}']['puntuacion'].update({'pa':pa})
                        # pp = novato[f'{p1}']['puntuacion']['pg'] + 1
                        # novato[f'{p1}']['puntuacion'].update({'pp':pp})
                        # tp = novato[f'{p1}']['puntuacion']['pg'] + 1
                        # novato[f'{p1}']['puntuacion'].update({'pp':tp})



                    # for x,y in novato.items():
                    #     if p1==x:
                    #         temp = y['puntuacion']['pj']
                    #         pj = temp + 1
                    #         y['puntuacion'].update({'pj':pj})
                    #     if p2==x:
                    #         temp = y['puntuacion']['pj']
                    #         pj = temp + 1
                    #         y['puntuacion'].update({'pj':pj})
                    # print(f'nov {novato}')
                    # torneo.update({'novato':novato})
                    # print(f'tro {torneo}')

                    print(novato)
                    os.system("pause")

                    return {'novato':novato}
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


