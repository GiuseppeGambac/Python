def ordinamento(giorno,mese,anno):
                                     # non sto a pensare ai bisestili
    
    if mese == 1:
        return giorno
    elif mese == 2:
        return 31+giorno
    elif mese ==3:
        return 31+28+giorno
    
    
    
    
print(ordinamento(2,3,2020))
