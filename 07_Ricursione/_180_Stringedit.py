def stringedit (parola1,parola2):
    
    if len(parola1) ==0:
        return len(parola2)
    elif len(parola2) ==0:
        return len(parola1)
    else:
        cost = 0
        
        if parola1[len(parola1)-1] != parola2[len(parola2)-1]:
            cost = 1
            
            d1 = stringedit(parola1[0: len(parola1) -1] , parola2) + 1
            d2 = stringedit(parola1,  parola2 [0: len(parola2) -1 ]) + 1
            d3 = stringedit(parola1[0:len(parola1) -1] , parola2[0:len(parola2) -1 ]) + cost  
            return min(d1,d2,d3)
        
        
        
print(stringedit("kitten","sitting"))
            
    