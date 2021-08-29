print("inserisci un numero in bit")

x =str(input())
totalenumero = 0

lunghezza = len(x ) -1

for i in range(lunghezza):
 
  if x[lunghezza -i] == "1":
        numero= 2**i
        totalenumero += numero
        
        
print(totalenumero)
      
  
      