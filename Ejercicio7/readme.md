**EJERCICIO 7**
* Problema: 
	* Se requiere realizar un programa para de la gestión de inventarios que permita realizar el control detallado de productos en un negocio. Cada producto estará caracterizado por los siguientes atributos:
		* Código del producto.
		* Nombre del producto.
		* Valor de compra del producto.
		* Valor de venta del producto.
		* Stock mínimo permitido.
		* Stock máximo permitido.
		* Nombre del proveedor del producto.
	* El programa debe tener un menú con las siguientes opciones
		1. Registro de Productos
		2. Visualización de Productos
		3. Actualización de Stock
		4. Informe de Productos Críticos
		5. Cálculo de Ganancia Potencial
		6. Salir

* Solución: 
	* El programa se va a dividir en 3 módulos: **Ejercicio7** que será el modulo principal, **menu** modulo que se encargara de la impresión y captura de selección del menú y **funciones** modulo en el cual se realizaran todos los cálculos y funciones que se requiera.
		* Modulo **Ejercicio7** : en este modulo se ejecuta el programa y se remite a cada submódulo necesario; además se utiliza para confirmar si el usuario quiere continuar trabajando en la misma opción o salir al menú principal.
		* Modulo **menu**: se definen las funciones:
			* menuPPal() : imprime el menú de opciones, solicita una opción numérica para el menú y valida que sea un dato de ingreso correcto, regresa a **Ejercicio7** la opción de menú seleccionado.
		* Modulo **funciones** : se definen las funciones:
			* valid() : función encargada de validar los diferentes datos ingresados por el usuario.
			* registrar() : función encargada de solicitar todos los datos referentes al producto que se va a registrar, además lo agrega en una lista llamada producto, al retornar al menú principal lo agrega en una lista general llamada invent.
			* ver() : función encargada de mostrar cada uno de los productos existentes en el inventario.
			* actStock() : función encargada de modificar los inventarios, ya sea añadir o disminuir stock dependiendo de lo que el usuario requiera.
			* informe() : función encargada de verificar si el inventario existente es menor que el stock mínimo permitido e imprimirlo al usuario.
			* ganancia () : función encargada de calcular la ganancia potencial considerando la diferencia entre el valor de venta y el valor de compra de cada producto, multiplicada por la cantidad en stock
* Variable:
	 Variable	|	in/out	|	Tipo|Descripcion
	-----------|-----------|----|--------
	 opMenu|	in	| int| Opción del menú principal que el usuario elige
  nombre| in| str|Nombre de la ciudad
  compra|in|float|Valor d compra del producto
  venta|in|float|Valor de venta del producto
  sMin|in|int|Stock minimo permitido del producto
  sMax|in|int|Stock maximo existente del producto
  proveedor|in|str|Nombre del proveedor del producto
  invent|out|list|Lista principal que almacena en cada item la informacion de cada producto
  producto|out|list|Sublista que almacena la informacion completa del producto
  tempCod|in|str|Variable temporal que solicita código del producto a modificar el stock
  tempModif|in|int|Variable que el usuario ingresa con la cantidad de stock a modificar
