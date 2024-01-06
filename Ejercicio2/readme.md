**EJERCICIO 2**
* Problema: 
	* Se requiere realizar un programa que permita calcular el IMC de los estudiantes nuevos de campuslands; el programa debe mostrar el nombre del estudiante, la edad, el IMCy la categoría según el IMC obtenido.

* Solución: 
	* Se debe realizar la validación de cada dato ingresado comprobando que cumpla con las características del mismo; para ello se puede usar una función general.
	* Se deben solicitar cada uno de los datos al usuario. como nombre, edad, peso y estatura.
	* Una vez verificados los valores se realiza el calculo del IMC bajo la ecuación:

		* $\ IMC = \frac{peso[Kg]}{estatura^2[m]}$
	* Con el IMC calculado se selecciona la categoría según corresponda para darle la salida al usuario con la información solicitada.
* Variable:
	 Variable	|	in/out	|	Tipo
	-----------|-----------|----
	 nombre|	in	| str
  edad| in| int
  peso|in|float
  estatura|in|float
  imc|out|	float
