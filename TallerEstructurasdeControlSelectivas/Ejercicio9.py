"""
Entradas
Nombre-->str-->Nombre
Monto de la compra-->float-->MC
salidas
Monto a pagar-->float-->MP
Descuento-->float-->Descuento
"""
#entrada
Nombre=str(input("Digite el nombre del cliente:"))
MC=float(input("Digite el monto de la compra:"))
#caja negra
if(MC<50000):
    Descuento=0
    MP=(MC*Descuento)
    Descuento=(MC-MP)

elif(MC<50000 and MC<=100000):
    Descuento=0.05
    MP=(MC*Descuento)
    Descuento=(MC-MP)

elif(MC<100000 and MC<=7000000):
    Descuento=0.11
    MP=(MC*Descuento)
    Descuento=(MC-MP)

elif(MC<700000 and MC<=1500000):
    Descuento=1.18
    MP=(MC*Descuento)
    Descuento=(MC*MP)
elif(MC<1500000):
    Descuento=0.25
    MP=(MC*Descuento)
    Descuento=(MC*mMP)
#salida
print("Nombre del cliente:"+str(Nombre))
print("El monto de la compra es:"+str(MC))
print("El monto a pagar es de:"+str(MP))
print("El descuento es de:"+str(Descuento))