"""
Entradas
Dia-->int-->d
Mes-->int-->m
Año-->int-->a
Salida
Signo-->str-->signo
Edad-->int-->edad
"""
#entrada
d=int(input("Digite el dia de su nacimiento:"))
m=int(input("Digite el mes de nacimiento:"))
a=int(input("Digite el año de su nacimiento:"))
#caja negra
if((d>=22 and m==11) or (d<=21 and m==12)):
    signo="Sagitario"
elif((d>=22 and m==12) or (d<=20 and m==1)):
    signo="Capricornio"
elif((d>=21 and m==1) or (d<=19 and m==2)):
    signo="Acuario"
elif((d>=20 and m==2) or (d<=19 and m==3)):
    signo="Piscis"
elif((d>=21 and m==3) or (d<=20 and m==4)):
    signo="Aries"
elif((d>=21 and m==4) or (d<=21 and m==5)):
    signo="Tauro"
elif((d>=22 and m==5) or (d<=21 and m==6)):
    signo="Geminis"
elif((d>=22 and m==6) or (d<=22 and m==7)):
    signo="Cancer"
elif((d>=23 and m==7) or (d<=23 and m==8)):
    signo="Leo"
elif((d>=24 and m==8) or (d<=22 and m==9)):
    signo="Virgo"
elif((d>=23 and m==9) or (d<=22 and m==10)):
    signo="Libra"
elif((d>=23 and m==10) or (d<=21 and m==11)):
    signo="Escorpion"
#salida
print("El signo correspondiente es:"+str(signo))
print("La edad es:"+str(2021-a))