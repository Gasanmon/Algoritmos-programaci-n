"""
Entradas:
MATEMATICAS
Examen matem ---> flotar ---> matex
tarea 1 ---> flotar ---> mat1
tarea 2 ---> flotar ---> mat2
tarea 3 ---> flotar ---> mat3
FISICA
examen fisica ---> flotar ---> fiex
tarea 1 ---> flotar ---> fi1
tarea 2 ---> flotar ---> fi2
QUIMICA
examen quimica ---> flotar ---> quimex
tarea 1 ---> flotar ---> quim1
tarea 2 ---> flotar ---> quim2
tarea 3 ---> flotar ---> quim3
Salidas:
Promedio matematicas ---> flotador ---> avmat
promedio fisica ---> flotar ---> avfi
promedio quimica ---> flotar ---> avquim
promedio general ---> float-promedio

"""
imprimir ( "Matematicas:" )
matex = float ( input ( "Nota del examen:" ))
mat1 = float ( input ( "Nota de la tarea 1:" ))
mat2 = float ( input ( "Nota de la tarea 2:" ))
mat3 = float ( input ( "Nota de la tarea 3:" ))
avmat = ( matex * 0.9 ) + ((( mat1 + mat2 + mat3 ) / 3 ) * 0.1 )
imprimir ( "Fisica:" )
fiex = float ( input ( "Nota del examen:" ))
fi1 = float ( input ( "Nota de la tarea 1:" ))
fi2 = float ( input ( "Nota de la tarea 2:" ))
avfi = ( fiex * 0.8 ) + ((( fi1 + fi2 ) / 2 ) * 0.2 )
print ( "Química:" )
quimex = float ( input ( "Nota del examen:" ))
quim1 = float ( input ( "Nota de la tarea 1:" ))
quim2 = float ( input ( "Nota de la tarea 2:" ))
quim3 = float ( input ( "Nota de la tarea 3:" ))
avquim = ( quimex * 0.85 ) + ((( quim1 + quim2 + quim3 ) / 3 ) * 0.15 )
promedio = (( avmat + avfi + avquim ) / 3 )
print ( "Promedio Matematicas:" + str ( avmat ))
print ( "Promedio Fisica:" + str ( avfi ))
print ( "Promedio Química:" + str ( avquim ))
print ( "Promedio General:" + str ( promedio ))