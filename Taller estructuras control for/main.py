archivo = open('paises.txt', 'r')
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""  
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la letra M
"""  
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="M"):
    print(i)
"""

#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
lista=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  pais.append(a)
  lista=[]
for i in pais:
  if(i[0]=="U"):
    print(i)
lista2=[]
capital=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  capital.append(a)
  lista=[]
for i in capital:
  if(i[0]=="u"):
    print(i)
"""

#Cuente e imprima cuantos paises que hay en el archivo
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  c=c+1
print(len(lista))
"""

#Busque e imprima la ciudad de Singapur
"""
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a=="Singapur: Singapur\n"):
    break
  lista=[]   
print(a)
"""

#Busque e imprima el pais de Venezuela y su capital
"""
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a=="Venezuela: Caracas\n"):
    break
  lista=[]   
print(a)
"""

#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="E"):
    print(i)
"""

#Buesque e imprima la Capiltal de Colombia
"""
palabra="Colombia:Bogotá"
a=palabra.index(":")
lista=[]
for i in range(a+1,len(palabra)):
  lista.append(palabra[i])
unir="".join(lista)
print(unir)
"""

#imprima la posicion del pais de Uganda
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
"""

#imprima la posicion del pais de Mexico
"""
x=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  x=x+1 
  if(a=="México: Ciudad de México \n"):
    break
  lista=[]   
print(x)
"""

#El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
"""
lista=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  if(a=="Madagascar: rey julien\n"):
    break
lista2=[]
for i in archivo:
  a=i.index(":")
for i in range(0,len(i)):
  lista2.remove("rey julien")
  lista2.insert("Madagascar: Antananarivo")
  print(lista2)
"""

#Agregue un país que no esté en la lista 
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Paises\n"):
    break
b=a.index(":")
lista2=[] 
for i in range(0,len(a)):
      lista2.append(a[i])
lista2.insert(0,"Escocia: Hogwarts \n")
unir="".join(lista2)
print(unir)
"""

archivo.close()
