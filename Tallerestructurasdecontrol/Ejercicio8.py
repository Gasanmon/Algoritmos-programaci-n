"""
Entradas:
Ladoa -> flotar -> la
ladob -> flotar -> lb
ladoc -> flotar -> lc
salidas:
semiperimetro -> flotar -> p
área -> flotar -> A

"""
la = float ( input ( "Insertar valor de lado la:" ))
lb = float ( input ( "Insertar valor de lado lb:" ))
lc = float ( input ( "Insertar valor de lado lc:" ))
pa= (( la + lb + lc ) / 2 )
A = (( p * ( p - la ) * ( p - lb ) * ( p - lc )) ** 0.5 )
print ( "El area del triangulo es:" + str ( A ))