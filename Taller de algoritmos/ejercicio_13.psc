Algoritmo  Inicio_Distancia_Dos_Puntos
	// VARIABLES :
	// X1 = abcisa1
	// Y1 = ordenada  2
	// X2 = abcisa  2
	// Y2 = ordenada  2
	// D = Distancia  entre  dos  puntos ( X , Y )
	Definir  X1 , X2, Y1, Y2, D Como Real
	
	Escribir  sin saltar "Insertar valor X1:"
	Leer  X1
	Escribir  sin saltar "Insertar valor Y1"
	Leer  Y1
	Escribir  sin saltar "Insertar valor X2:"
	Leer  X2
	Escribir  sin saltar "Insertar valor y2:"
	Leer  Y2
	
	D = RC (( X2 - X1 ) ^ 2 + ( Y2 - Y1 ) ^ 2 )
	
	Escribir  "La distancia entre los puntos P1 Y P2 es:" , D ;
	
FinAlgoritmo
