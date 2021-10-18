"""
Entradas
Venta -> flotador -> Venta
Salidas
Descuento -> flotador -> D
Valor total -> flotar -> total

"""
Venta = float ( input ( "Digite la venta:" ))
D = ( Venta * 0,15 )
total = ( Venta - D )
print ( "valor de descuento:" + str ( D ), "valor a pagar:" + str ( total ))