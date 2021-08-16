print("inserisci il numero dei lati di una forma geoemtrica")

lati = int(input())




if lati == 3:
    print("è un triangolo")
elif lati == 4:
    print("è un quadrato")
elif lati > 10:
    print("errore")   