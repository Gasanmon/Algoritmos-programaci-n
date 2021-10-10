Algoritmo  Inicio_Comision
	Escribir  "Digite las tres ventas al dia"
	Leer  venta1
	Leer  venta2
	Leer  venta3
	c1 <- (( venta1 * 10 ) / 100 )
	c2 <- (( venta2 * 10 ) / 100 )
	c3 <- (( venta3 * 10 ) / 100 )
	Escribir  "Comision de venta 1: $"  c1
	Escribir  "Comision de venta 2: $"  c2
	Escribir  "Comision de venta 3: $"  c3
	ct <- ( c1 + c2 + c3 )
	Escribir  "La comision total es de: $"  ct
	
FinAlgoritmo
