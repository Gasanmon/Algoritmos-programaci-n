"""
Entradas
LecturaAnterior-->int-->Lan
LecturaActual-->int-->Lac
Salidas
TotalCapital-->int-->T
"""
#entrada
Lan=int(input("Ingrese la lectura anterior: "))
Lac=int(input("Ingrese la lectura actual: "))
#caja negra
a=Lac-Lan
if(a>=0 and a<=100):
  T=4600
elif(a>=101 and a<=300):
  T=80000
elif(a>=301 and a<=500):
  T=100000
elif(a>=501):
  T=120000
#salida
print("El monto a pagar es:"+str(T))