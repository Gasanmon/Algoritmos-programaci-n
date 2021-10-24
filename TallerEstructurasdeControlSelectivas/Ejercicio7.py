"""
Entrada
Distancia-->float-->D
Salida
Valor a pagar-->float-->V
"""
#entrada
Distancia=float(input("Digite la distancia recorrida:"))
#caja negra
if(Distancia<300):
    V=50000
    print("El valor a pagar es:"+str(V))
elif((Distancia>=300) and(Distancia<1000)):
    V=(((Distancia-300)*30000+70000))
    print("El valor a pagar es:"+str(V))
elif(Distancia>1000):
    V=(((Distancia-300)*9000+150000))
    print("El valor a pagar es:"+str(V))
    