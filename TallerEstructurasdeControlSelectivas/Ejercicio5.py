"""
Entrada
Salario base-->float-->SB
Ventas departamento1-->float-->dep1
Ventas departamento2-->float-->dep2
Ventas departamento3-->float-->dep3

Salidas
Venta total-->float-->VT
"""
#entrada
SB=float(input("Digite el sueldo base:"))
dep1=float(input("Digite el valor de ventas departamento 1:"))
dep2=float(input("Digite el valor de ventas departamento 2:"))
dep3=float(input("Digite el valor de ventas departamaneto 3:"))
#caja negra
a=dep1+dep2+dep3
b=(33*a)/100
#salida
if(dep1>b):
    print("El salario del departamento 1 es de:"+str(SB+(SB*0.20)))
else:
    print("El salario del departamento 1 es de:"+str(SB))
if(dep2>b):
    print("El salario del departamento 2 es de:"+str(SB+(SB*0.20)))
else:
    print("El salario del departamento 2 es de:"+str(SB))
if(dep3>b):
    print("El salario del departamento 3 es de:"+str(SB+(SB*0.20)))
else:
    print("El salario del departamento 3 es de:"+str(SB+(SB*0.20)))