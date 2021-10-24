"""
Entrada
Monto Total-->float-->M
Cantidad a pagar po piezas-->float-->C
Salidas
Valor-->float-->V
Inversion-->float-->I
Prestamo bancario-->float-->Prestamo
Credito bancario-->float-->CB
Monto a pagara por intereses-->float-->Intereses
"""
#entrada
M=int(input("digite el numero de piezas:"))
C=float(input("Digite el valor de cada pieza:"))
V=(M*C)
#Caja negra
if(V<5000000):
    I=(V*0.7)
    CB=(V*0.3)
    Intereses=(V*0.2)
   
else:
    I=(V*0.55)
    Prestamo=(V*0.3)
    Intereses=(V*0.2)
    CB=(V*0.15)
#salida
print("el valor que le corresponde pagar a la empresa es:"+str(I))
print("El valor del credito bancario es:"+str(CB))
print("El valor del interes es de:"+str(Intereses))
print("El valor que le corresponde pagar a la empresa es:"+str(I))
print("El valor del credito bancario es:"+str(CB))
print("El valor del interes es de:"+str(Intereses))
print("El valor del prestamo del banco es de:"+str(Prestamo))