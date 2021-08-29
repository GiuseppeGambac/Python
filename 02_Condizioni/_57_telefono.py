minuti = int(input())
messaggi = int(input())

costo = 15.0
conteggio = 0
conteggio2 = 0
if minuti > 50:
    resto = minuti - 50
    conteggio = resto // 1
    costo += conteggio * 0.25
    
    
if minuti > 50:
    resto = minuti - 50
    conteggio2 = resto // 1
    costo += conteggio2 * 0.15
    
    
# chiamata 911

costo += 0.44

tasse = costo * 1.05
print("%.2f"  %tasse)
if conteggio > 0:

    print(conteggio *0.25)
    
if conteggio2 > 0:
    
    print(conteggio2 *0.15)
