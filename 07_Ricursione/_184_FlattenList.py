def Flatterlist(lista):
    if lista ==[]:
        return []
    
    if type[lista[0]] == list:
       return Flatterlist(lista[0]) + Flatterlist(lista[1:])
    else:
        return [lista[0]] + Flatterlist(lista[1:])
    
                                                            # ho provato la soluzione del libro ma non funziona
    
    
lista = [1,[2,3],[[4,5,6]],7]

lista1 =1,2,3,4,5,6


        