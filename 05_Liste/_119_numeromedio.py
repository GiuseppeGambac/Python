ingresso = input()
somma = 0
conteggio = 0
lista =[]
minori =[]
maggiori = []


while ingresso != "":
    
    numero = int(ingresso)
    somma += numero
    conteggio += 1
    lista.append(numero)
    ingresso =input()
    
    
media = somma /conteggio


for i in range(len(lista)):
    
    if lista[i] < media:
        minori.append(lista[i])
    elif lista[i] > media:
        maggiori.append(lista[i])
        
        
print(minori)
print(media)
print(maggiori)
        
    
    
    
    
    
    
