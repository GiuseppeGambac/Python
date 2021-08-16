
from decimal import Decimal

totaleprezzi = 0
while True:
    print("inserisci un prezzo")
    prezzo = str(input())
    
    if prezzo == "":
        break
    
    totaleprezzi += float(prezzo)
    
    
if totaleprezzi > 2.5:
    modulo = 0.05 - (totaleprezzi % 0.05)            # Calcolo il modulo e poi lo sottraggo a 0.05 così so quanto manca

    prezzoarrotondato = totaleprezzi + modulo        # aggiungo quella differenza 

        
    print(totaleprezzi)
    print(prezzoarrotondato)
else:
    modulo2 = 1 (totaleprezzi % 0.05)                # calcolo il modulo
    
    prezzoarrotondato2 = totaleprezzi - modulo2      # e lo sottraggo in modo da arrivare all'ultima divisione
    print(totaleprezzi)
    print(prezzoarrotondato2)
    