**EJERCICIO 4**
* Problema: 
	* Se requiere un programa que permita ingresar n números enteros positivos y cuando se ingrese un numero negativo debe mostrar en pantalla el reporte:
		*  Total de números ingresados
		*  Total de números pares ingresados
		*  Promedio de los números pares
		*  Promedio de los números impares
		*  Cuantos números son menores que 10
		*  Cuantos números están entre 20 y 50
		*  Cuantos números son mayores que 100

* Solución: 
	* Se debe realizar la validación de cada numero ingresado comprobando que sean enteros positivos.
	* Mediante un iterativo **while** es posible solicitar los n números y realizar las validaciones necesarias para ir acumulando con contadores de cada item solicitado. 
	* las validaciones se realizan utilizando condicionales **if y elif** para ir contando cada item, 
	* Cuando el usuario ingrese un valor menor a 0 se validara con un condicional **if** adicional para hacer un **break** y finalizar el iterativo; posteriormente se imprimen las estadísticas solicitadas. 
* Variable:
	 Variable	|	in/out	|	Tipo|Descripcion
	-----------|-----------|----|--------
	 num|	in	| int|Numero solicitado al usuario
  cont| out| int|Contador numeros totales
  pares| out| int|Acumulador numeros pares (para calcular el promedio)
  impar| out| int|Acumulador numeros impares (para calcular el promedio)
  menor10| out| int|Contador numeros menores a 10
  inter| out| int|Contador numeros entre 20 y 50
  mayor10| out| int|Contador numeros mayores a 10
  contImpar| out| int|Contador numeros impares
  contPar| out| int|Contador numeros pares
