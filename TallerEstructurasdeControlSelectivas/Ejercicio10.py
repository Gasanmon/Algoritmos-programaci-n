"""
Entradas
Sueldo_bruto-->float-->SA
Salidas
Categoria-->int-->C
Sueldo_neto-->float-->SN
"""
#entrada
SA=float(input("Digite el salario bruto: "))
SN=0.0
#caja negra
if(SA>=5_000_000):
  sn=(SA*0.10)+SA
  C=1
elif(SA<5_000_000 and SA>=4_300_000):
  SN=(SA*0.15)+SA
  C=2
elif(SA<4_300_000 and SA>=3_600_000):
  sn=(SA*0.20)+SA
  C=3
elif(SA<3_600_000 and SA>=2_000_000):
  sn=(SA*0.40)+SA
  C=4
elif(SA<2_000_000 and SA>=900_000):
  SN=(SA*0.60)+SA
  C=5
#salida
print("La categoria es: "+str(C))
print("El sueldo neto es de: "+str(SN))