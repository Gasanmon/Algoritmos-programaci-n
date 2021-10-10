Algoritmo  Inicio_Horas_Minutos
	Escribir  "Digite la cantidad de minutos"
	Leer  minutos
	hora <- ( minutos / 60 )
	Hora <- Trunc ( hora )
	Restante <- ( minutos % 60 )
	minutos <- ( Restante )
	Escribir  "son"  hora  "horas y"  minutos  "minutos"
	
FinAlgoritmo
