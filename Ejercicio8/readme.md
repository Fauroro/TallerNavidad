**EJERCICIO 8**
* Problema: 
	* Se requiere realizar un programa que permita llevar el control de los juegos llevados a cabo por cada uno de los Inscritos en el torneo.

* Solución: 
	* El programa se va a dividir en 4 módulos: **Ejercicio8** que será el modulo principal, **menu** modulo que se encargara de la impresión y captura de selección del menú, **funciones** modulo en el cual se realizaran todos los cálculos y funciones que se requiera y **resultados** modulo encargado de solicitar los resultados de los partidos.
		* Modulo **Ejercicio8** : en este modulo se ejecuta el programa y se remite a cada submódulo necesario; además se utiliza para confirmar si el usuario quiere continuar trabajando en la misma opción o salir al menú principal.
		* Modulo **menu**: se definen las funciones:
			* menuPPal() : imprime el menú de opciones, solicita una opción numérica para el menú y valida que sea un dato de ingreso correcto, regresa a **Ejercicio8** la opción de menú seleccionado.
		* Modulo **funciones** : se definen las funciones:
			* registrar() : función encargada de registrar cada jugador segun la categoría que el usuario seleccione usando para esto la funcion subReg() 
			* suReg() : función encargada de validar si el jugador corresponde a la categoría usando la edad, también solicita datos del jugador adicionales se adiciona en un diccionario junto con los demás items necesarios; una vez retorna a la función registrar() se agrega en un diccionario de la categoría usando un id generado automáticamente como Key; y al retornar al menú principal se adiciona dicha información a un diccionario general llamado  torneo; cada información se adiciona con la categoría como Key.
			* tabla() : función encargada de mostrar la información detallada de los jugadores dependiendo de la categoría seleccionada.
			* campeon() : función encargada de seleccionar el campeón de la categoría que el usuario seleccione.
		* Modulo **resultados** : se definen las funciones:
			* puntuacion() : función encargada de verificar que la categoría que el usuario selecciona para registrar los resultados este habilitada según el numero de inscritos
			* marcadores() : función encargada de solicitar los sets jugados, ID de los jugadores de un listados de los jugadores inscritos y las puntuaciones de cada set, esto con el fin de acumular los puntos a favor y en contra de cada jugador y así obtener el ganador del juego y sumar puntos totales usando la función winSet()
			* winSet() : funcion encargada de registrar en el diccionario correspondiente los resultados de los jugadores que participaron en el partido
* Variable:
	 Variable	|	in/out	|	Tipo|Descripcion
	-----------|-----------|----|--------
	 opMenu|	in	| int| Opción del menú principal que el usuario elige
  nombre| in| str|Nombre del jugador
  edad|in|int|Edad del jugador
  id|out|int|ID unico generado automáticamente de cada jugador
  torneo|out|dict|Diccionario principal que almacena todos los datos del torneo
  novato|out|dict|Diccionario que almacena la informacion completa los jugadores de la categoria novato.
    intermedio|out|dict|Diccionario que almacena la información completa los jugadores de la categoría intermedio.
     avanzado|out|dict|Diccionario que almacena la información completa los jugadores de la categoría avanzado.
     jugador|out|dict|Diccionario que almacena la informacion completa de puntuacion y datos del jugador.
  sets|in|int|Cantidad de sets jugados en el partido
  p1|in|int|ID del jugador 1 del partido
  p2|in|int|ID del jugador 2 del partido
  marc1|in|int|Puntos marcados por el jugador 1 en el set
  marc2|in|int|Puntos marcados por el jugador 2 en el set
