"""
Entrada
A-->int-->A
B-->int-->B
C-->int-->C
D-->int-->D
Salidas
valor total-->int-->vt
"""
#entrada
A=int(input("Digite el valor A:"))
B=int(input("Digite el valor B:"))
C=int(input("Digite el valor C:"))
D=int(input("Digite el valor D:"))
N1=A
N2=B
N3=C
N4=D
#caja negra
if(C>5):
    C=0
    D=0
    B=B+1
elif(C<5):
    C=0
    D=0
elif(C==5):
    D=0
#salida
print("el valor aproximado es:"+str(N1)+str(N2)+str(N3)+str(N4))