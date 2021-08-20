def conteggio(lista,minimo,massimo):
    conteggio = 0
    for i in range(len(lista)):
        if lista[i] >= minimo or lista[i] < massimo:
            conteggio +=1
            
    return conteggio





lista = [1,3,4,50,30]

print(conteggio(lista,2,100))

           
        
            
    