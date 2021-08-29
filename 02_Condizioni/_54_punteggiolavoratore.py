
punteggio = float(input(" punteggio: "))

if punteggio == 0:
 performance = "inaccettabile"
elif punteggio == 0.4:
 performance = "accettabile"
elif punteggio >= 0.6:
 performance = "Merito"
else:
 performance = ""
 
 
if performance =="":
    print("errore")
else:
    print(performance)
    print(punteggio * 2400)