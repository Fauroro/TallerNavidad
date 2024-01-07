**EJERCICIO 6**
* Problema: 
	* Se requiere realizar un programa que permita calcular el valor de CO2 producido en diferentes dependencias.
	* El programa debe tener un menú con las siguientes opciones
		1. Registrar Dependencia
		2. Registrar consumo por dependencia
		3. Ver CO2 producido
		4. Dependencia que produce mayor CO2
		5. Salir

* Solución: 
	* El programa se va a dividir en 4 módulos: **Ejercicio6** que será el modulo principal, **menu** modulo que se encargara de la impresión y captura de selección del menú, **funciones** modulo en el cual se realizaran todos los cálculos y funciones que se requiera y **consumo** modulo encargado de realizar el calculo de produccion de CO2 por dependencia y el mayor.
		* Modulo **Ejercicio6** : en este modulo se ejecuta el programa y se remite a cada submódulo necesario; además se utiliza para confirmar si el usuario quiere continuar trabajando en la misma opción o salir al menú principal.
		* Modulo **menu**: se definen las funciones:
			* menuPPal() : imprime el menú de opciones, solicita una opción numérica para el menú y valida que sea un dato de ingreso correcto, regresa a **Ejercicio6** la opción de menú seleccionado.
		* Modulo **funciones** : se definen las funciones:
			* registrar() : función encargada de registrar cada dependencia ingresada por el usuario en una lista, además de agregar un espacio vacío para registrar los consumos mas adelante; una vez retorna al menú principal se agrega en la lista general que almacena todas las dependencias.
			* consumo() : función encargada de buscar la dependencia en la cual se registraran los consumos, el usuario podrá seleccionar si el consumo es el general o si lo quiere ingresar por la potencia nominal de cada equipo; adicional el modulo se encarga de guardar y convertir los consumos a una misma convención de unidades y  almacenarlos en la dependencia que le corresponda.
		* Modulo **consumo** : se definen las funciones:
			* produccion() : función encargada de calcular el consumo neto de cada dependencia y el consumo general y adicional se lo muestra al usuario.
			* mayor() : función encargada de encontrar la dependencia con el consumo de CO2 mas alto de las dependencias registradas e imprimirlo al usuario.
* Variable:
	 Variable	|	in/out	|	Tipo|Descripcion
	-----------|-----------|----|--------
	 opMenu|	in	| int| Opción del menú principal que el usuario elige
  nombre| in| str|Nombre de la dependencia
  dependencia|out|list|Lista principal que almacena en cada item la informacion de cada dependencia
  depend|out|list|Sublista que almacena la informacion completa del dependencia y su consumo
  dep|in|str|Variable temporal que solicita nombre de la dependencia a registrar consumos
  opCons|in|int|Variable que el usuario ingresa con la selección del tipo de consumo
  consumo|in|float|Consumo del equipo/general
  tiempo|in|float|Duracion aproximada de uso del cada equipo que se esta registrando
  co2|out|float|CO2 producido por el equipo/general
  prodDepend|out|float|Acumulador de consumos de una dependencia
  prodTotal|out|float|CO2 producido en Total de todas las dependencias
  
  
