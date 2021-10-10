Algoritmo  Inicio_Vehiculos_Distancia
	Escribir  "Ingrese la velocidad del vehiculo de adelante en Km / h"
	Leer  v1
	Escribir  "Ingrese la velocidad del vehiculo de atras en Km / h"
	Leer  v2
	
	si  v2 > v1 Entonces
		
		Escribir  "Ingrese la distancia en Km"
		Leer  D
		Tiempo <- D / ( v2 - v1 )
		minutos <- Tiempo * 60
		Escribir  "Lo alcanzara en"  minutos  "minutos"
		
	SiNo
		
			Escribir  "---- Error ------ la velocidad del vehiculo de atras debe ser mayor"
		FinSi
		
	
FinAlgoritmo
