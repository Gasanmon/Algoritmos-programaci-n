"""
Entradas
Temperatura-->float-->T
Salidas 
Deporte-->float-->D
"""
#entrada
T=float(input("Ingrese la temperatura: "))
D=""#str
#caja negra
if(T>85):
  D="Natacion"
elif(T>70 and T<=85):
  D="Tenis"
elif(T>32 and T<=70):
  D="Golf"
elif(T>10 and T<=32):
  D="Esqui"
elif(T<=10):
  D="Marcha"
#salida
print("El deporte que puede practicar es: "+str(D))