"""
Entrada

A-->int-->A
B-->int-->B
C-->int-->c
D-->int-->D
Salidas
Expresion1-->int-->Expresion1
Expresion2-->int-->Expresion2
"""
#entrada
A=int(input("Digite el valor A:"))
B=int(input("Digite el valor B:"))
C=int(input("Digite el valor C:"))
D=int(input("Digite el valor D:"))
#caja negra
if(D==0):
    Expresion1=(A-C)**2 
elif(D>0):
    Expresion2=((A-B)**3)/D
    
#salida
print("El resultado es:"+str(Expresion1))
print("El valor es:"+str(Expresion2))