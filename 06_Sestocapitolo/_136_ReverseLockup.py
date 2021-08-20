def ReverseLockup(dizionario,valore):
    lista =[]
    """
    listavalori = list(dizionario.values())
    listakey = list(dizionario.keys())
    
    
    for i in range(len(listakey)):
       if valore == listavalori[i]:           #MODO ARTIGIANALE PER FARLO
        lista.append(listakey[i])
        """
        
    for i in dizionario:
        if dizionario[i] ==valore:
            lista.append(i)
    return lista
        
        
        
        
dizionario ={"uno" : 1,  "due" : 2 , "tre" : 2  }



print(ReverseLockup(dizionario,2))
        
        
    