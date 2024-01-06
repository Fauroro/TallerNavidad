**EJERCICIO 3**
* Problema: 
	* Se requiere realizar un programa que permita calcular el IMC de los estudiantes nuevos de campuslands; además se requiere tener el registro de 20 estudiantes y poder determinar el estado de salud de la comunidad estudiantil;

* Solución: 
	* Se debe realizar la validación de cada dato ingresado comprobando que cumpla con las características del mismo; para ello se puede usar una función general.
	* Se deben solicitar cada uno de los datos al usuario. como nombre, edad, peso y estatura; esto para cada uno de los estudiantes que se ingresen hasta completar 20; esto se hace realizando un bucle **for**
	* Una vez verificados los valores se realiza el calculo del IMC bajo la ecuación:

		* $\ IMC = \frac{peso[Kg]}{estatura^2[m]}$
	* Con el IMC calculado se selecciona la categoría según corresponda y se acumula en un contador de tal manera que se pueda regresar al usuario la cantidad de estudiantes en cada categoría.
* Variable:
	 Variable	|	in/out	|	Tipo
	-----------|-----------|----
	 nombre|	in	| str
  edad| in| int
  peso|in|float
  estatura|in|float
  imc|out|	float
  insuf|out|int
  ideal|out|int
  obesidad1|out|int
  obesidad2|out|int
  obesidad3|out|int
  sobrepeso|out|int
