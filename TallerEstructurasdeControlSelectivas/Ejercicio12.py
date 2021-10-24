"""
Entradas
Cantidad de dinero-->float-->cd
Salidas
Cantidad de billetes-->float-->cb
"""
#entrada
cd=float(input("Digite la cantidad de dinero:"))
#caja negra
b=cd
b100000=(b-b%100000)/100000
b=b%100000
b50000=(b-b%50000)/50000
b=b%50000
b20000=(b-b%20000)/20000
b=b%20000
b10000=(b-b%10000)/10000
b=b%10000
b5000=(b-b%5000)/5000
b=b%5000
b2000=(b-b%2000)/2000
b=b%2000
b1000=(b-b%1000)/1000
b=b%1000
mo500=(b-b%500)/500
b=b%500
mo200=(b-b%200)/200
b=b%200
mo100=(b-b%100)/100
b=b%100
mo50=(b-b%50)/50
b=b%50
#salida
print("La cantidad de billetes de 100000 es:"+str(b100000))
print("La cantidad de billetes de 50000 es:"+str(b50000))
print("La cantidad de billetes de 20000 es:"+str(b20000))
print("La cantidad de billetes de 10000 es:"+str(b10000))
print("La cantidad de billetes de 5000 es:"+str(b5000))
print("La cantidad de billetes de 2000 es:"+str(b2000))
print("La cantidad de billetes de 1000 es:"+str(b1000))
print("La cantidad de monedas de 500:"+str(mo500))
print("La cantidad de monedas de 200:"+str(mo200))
print("La cantidad de monedas de 100:"+str(mo100))
print("La cantidad de modenas de 50:"+str(mo50))