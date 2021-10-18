"""
Entradas:
Horas trabajadas ---> flotar ---> horast
precio ---> flotar ---> precio
Salidas:
Salario bruto ---> flotador ---> sbrut
descuentos ---> flotar ---> desc
salario neto ---> float ---> stotal

"""
horast = float ( input ( "Ingrese el número de horas trabajadas:" ))
precio = float ( input ( "Ingrese el valor por cada hora de trabajo:" ))
sbrut = ( horast * precio )
desc = ( sbrut * 0.2 )
stotal = ( sbrut - desc )
print ( "El salario total es:" + str ( stotal ))