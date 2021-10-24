"""
Entradas
P-->int-->P
Q-->int-->Q
Salidas
Expresion-->int-->E
"""
#entrada
P=int(input("Digite el valor de P:"))
Q=int(input("Digite el valor de Q:"))
E=(P**3)+(Q**4)-(2*(P**2))
#caja negra
if(E<=680):
   print("P y Q satisfacen la expresion")
else:
    print("P y Q no satisfacen la expresion")