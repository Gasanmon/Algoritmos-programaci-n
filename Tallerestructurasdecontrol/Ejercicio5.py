"""
Entradas
Parcial1 -> flotar -> P1
Parcial2 -> flotar -> P2
Parcial3 -> flotar -> P3
Examenfinal -> flotar -> Ef
Trabajofinal -> flotador -> Tf
Salidas
Promedioparciales -> flotar -> Promp
Notadefinitiva -> flotar -> Notafinal

"""
P1 = float ( input ( "Nota del parcial 1:" ))
P2 = float ( input ( "Nota del parcial 2:" ))
P3 = float ( input ( "Nota del parcial 3:" ))
Ef = float ( input ( "Nota examen final:" ))
Tf = float ( input ( "Nota del trabajo final:" ))
Mensaje = (( P1 + P2 + P3 ) / 3 )
Notafinal = (( Promp * 0.55 ) + ( Ef * 0.33 ) + ( Tf * 0.15 ))
print ( "Nota definitiva:" + str ( Notafinal ))