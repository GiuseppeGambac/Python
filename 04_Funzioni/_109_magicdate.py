import _106_giornimese as funzione

def datamagica(giorno,mese,anno):
    
    risultato = giorno * mese
    
    if risultato == anno % 100:
        return True
    return False


print(datamagica(13,12,2020))



for i in range(1900,2000):                                             # per ogni anno
    for x in range(1,13):                                              # per ogni mese
        for y in range(1, funzione.Giornimese(x, i) ):                 # per ogni giorno di quel mese
            if datamagica(y,x,i):
                print('%d %d %d' %(y,x,i))