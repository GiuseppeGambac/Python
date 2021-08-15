print("Numero di bottiglie di grandezza minore di un litro")
menolitro = int(input())
print("Numero di bottiglie di grandezza maggiore di un litro")
piulitro = int(input())



rimborsomenolitro = menolitro * 0.10
rimborsopiulitro = piulitro * 0.25

rimborsototale = rimborsomenolitro + rimborsopiulitro

print("%.2f$"  % rimborsototale)           # In questo modo posso formattare dei valori come voglio io 