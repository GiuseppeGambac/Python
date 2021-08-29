print("inserisci un intero di quattro cifre")

numero = int(input())


numerostringa = str(numero)

sommatotale = 0

for i in range (len(numerostringa)):
    
    singolonumero = int(numerostringa[i])        #prendo il valore di ogni lettera della stringa e man mano lo aggiungo a somma totale
    sommatotale += singolonumero


print(sommatotale)  

