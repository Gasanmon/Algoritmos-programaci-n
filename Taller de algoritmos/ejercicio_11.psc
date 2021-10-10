Proceso  Inicio_Calificaciones
	Escribir  "ingrese primera calificación"
	Leer  cal1
	Escribir  "ingrese segunda calificación"
	Leer  cal2
	Escribir  "ingrese tercera calificación"
	Leer  cal3
	
	Escribir  "ingrese calificacion del examen final"
	Leer  ef
	
	Escribir  "ingrese calificacion del trabajo final"
	Leer  tf
	
	promedio = ( cal1 + cal2 + cal3 ) / 3
	
	parcial =  promedio * 0.55
	pef =  ef * 0.30
	ptf =  tf * 0.15
	
	Alumno =  parcial + pef + ptf
	
	Imprimir  "su calificacion final es:" Alumno 
	
FinAlgoritmo
