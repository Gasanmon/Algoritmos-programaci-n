Algoritmo  Inicio_RaizCuadrada_RaizCubica
	Escribir  "1 raiz cuadrada"
	Escribir  "2 raiz cubica"
	Leer  opc
	Segun  opc Hacer
		
		1 :
			Escribir  "Digitar un numero:"
			Leer  num1 
			num2 <- rc ( num1 )
			Escribir  "El resultado de la raiz cuadrada de" , num1  "es:" , num2
			
		2 :
			Escribir  "Digitar un numero:"
			Leer  num3
			num4 <- rc ( num3 ) ^ ( 1 / 3 )
			Escribir  "El resultado de la raiz cuadrada de" , num3  "es:" , num4
	FinSegun
	
	
FinAlgoritmo
