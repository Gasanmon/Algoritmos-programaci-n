"""
Entradas:
precio final ---> float ---> p
precio de venta ---> flotador ---> pr
Salidas:
diferencia ---> flotar ---> dif
porcentaje descuento ---> float ---> desc

"""
p = float ( input ( "Digite el valor pagado:" ))
pr= float ( input ( "Ingrese el precio de venta sugerido:" ))
dif = ( pr - p )
desc = (( dif * 100 ) / pr )
print ( "El porcentaje de descuento fue:" + str ( desc ))