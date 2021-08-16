print("inserisci una parola")

parola = str(input())

lunghezzaparola =len(parola) -1

secondaparola = parola
for i in range(lunghezzaparola ):
    
    
   if  secondaparola[lunghezzaparola -i ] == parola[i]:
       uguale =True
   else:
       uguale =False
    
    

if uguale:
    print("è palindroma")
else:
    print("non è palindroma")