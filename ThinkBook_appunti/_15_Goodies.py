from collections import Counter
from collections import defaultdict

# condizioni


x = 0

if x >= 0:
  print("è positivo")
else:
  print("è negativo")
  
  
print("è positivo") if x >= 0 else print ("è negativo")   # modo alternativo






listastringhe = ["a","b","c"]
lista = []                                           # metodo normale per aggiungere a liste

for carattere in listastringhe:
    lista.append(carattere.capitalize())


lista2 = [l.capitalize() for l in listastringhe]    # metodo alternativo





any()
set()
Counter()
defaultdict()


#*args * kargvs