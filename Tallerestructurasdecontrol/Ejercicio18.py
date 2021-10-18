"""
Entradas:
Capital -> flotador -> cap
tiempo -> int -> Tiem
tasa -> flotar -> Tasa
Salidas:
Interes -> flotar -> Interes
Promedio -> flotar -> prom

"""
Cap = float ( input ( "Insertar capital:" ))
Tiem = int ( input ( "Insertar el tiempo de inversión:" ))
Tasa = float ( input ( "Insertar la tasa de interes:" ))
Interes = (( Cap * Tasa * Tiem ) / 100 )
Prom = ( Interes / Tiem )
print ( "El valor total de ineteres es:" +  str ( Interes ), "El porcentaje de interes por año es:" +  str ( Prom ), "%" )