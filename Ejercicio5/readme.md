**EJERCICIO 5**
* Problema: 
	* Se requiere realizar un programa que le permita llevar el registro de los sismos presentados en 5 ciudades del país. Por cada ciudad se realizan n cantidad de registros. El programa debe permitir registrar las muestras del movimiento en cada ciudad.
		* El programa debe tener un menú con las siguientes opciones
			1. Registrar Ciudad
			2. Registrar Sismo
			3. Buscar sismos por ciudad
			4. Informe de riesgo
			5. Salir

* Solución: 
	* El programa se va a dividir en 3 módulos: **Ejercicio5** que será el modulo principal, **menu** modulo que se encargara de la impresión y captura de selección del menú y **funciones** modulo en el cual se realizaran todos los cálculos y funciones que se requiera.
		* Modulo **Ejercicio5** : en este modulo se ejecuta el programa y se remite a cada submódulo necesario.
		* Modulo **menu**: se definen las funciones:
			* menuPPal() : imprime el menú de opciones, solicita una opción numérica para el menú y valida que sea un dato de ingreso correcto, regresa a **Ejercicio5** la opción de menú seleccionado.
		* Modulo **funciones** : se definen las funciones:
			* regCiudad() : función encargada de solicitar los datos de registro de las 5 ciudades como el nombre y almacenarlos en una lista junto con un  espacio vacío para el ingreso de cada registro; luego cada ciudad es agregada en una lista principal llamada sismos.
			* regSismo() : función encargada de navegar en la lista sismos para solicitar registro ciudad por ciudad que se encuentre registrada y agregarlos en la sublista para registros de cada ciudad.
			* buscar() : función encargada de mostrar las ciudades que se encuentran registradas para que el usuario seleccione la ciudad de la cual se quiera ver los registros existente, también imprime todos los registros de la ciudad que se selecciona.
			* informe() : funcion encargada de recorrer la lista de sismos e ir calculando el promedio de los registros de cada ciudad, tambien va clasificando e imprimiendo el nivel de riesgo en el cual se encuentra cada ciudad.

* Variable:
	 Variable	|	in/out	|	Tipo|Descripcion
	-----------|-----------|----|--------
	 opMenu|	in	| int| Opción del menú principal que el usuario elige
  nombre| in| str|Nombre de la ciudad
  sismos|out|list|Lista principal que almacena en cada item la informacion de cada ciudad
  ciudad|out|list|Variable que almacena la informacion de nombre y registros de cada ciudad
  suma|out|float|Variable encargada de acumular la sumatoria de movimientos teluricos para cada ciudad
  promedio|out|float|Variable utilizada para el calculo de promedios de los registros por ciudad

