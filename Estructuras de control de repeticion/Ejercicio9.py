a=0
g=0
d=0
while True:
    NUM=int(input())
    if (NUM==1):
        a+=1
    elif (NUM==2):
        g+=1
    elif (NUM==3):
        d+=1
    elif (NUM==4):
        break
print ("MUITO OBRIGADO")
print ("Alcool:",(a))
print ("Gasolina:",(g))
print ("Diesel:",(d))