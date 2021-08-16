print("inserisci una stringa")

parola = str(input())

lunghezzaparola =len(parola) -1

secondaparola = parola
for i in range(lunghezzaparola ):
    
    
   if  secondaparola[lunghezzaparola -i ] == parola[i]:      #uguale all'altro, funziona lo stesso
       uguale =True
   else:
       uguale =False
    
    

if uguale:
    print("è palindroma")
else:
    print("non è palindroma")