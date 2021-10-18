"""
Entradas:
venta en galones ---> float ---> cg
Salidas
venta en litros ---> float ---> lts
venta total ---> float ---> total

"""
cg = float ( input ( "Ingrese la venta en galones:" ))
lts = ( galones * 3.785 )
total = ( lts * 50000 )
print ( "El total de la venta es:" + str ( total ))