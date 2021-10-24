"""
Entrada

Salario bruto-->float--> SB
Salidas

Nuevo salario-->float-->NS
"""
#entrada
SB=float(input("Digite el sueldo bruto del trabajador:"))
#caja negra
if(SB<900000):
    NS= (SB*0.15)
    print("El nuevo salario es:"+str(NS))
elif(SB>900000):
    NS=(SB*0.12)
#Salida
print("El nuevo salario es:"+str(NS))