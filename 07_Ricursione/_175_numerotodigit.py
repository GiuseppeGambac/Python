def conversione(numero):
    if numero <0:
        return "errore"
    elif numero == 0:
        return  
    else:
        conversione(int(numero/2))             #34 viene diviso e diventa 17, il 34 non ha resto quindi stampo 0, il 17 diventa 8 e ha resto 1, 8 diventa 4 resto 0, 4 diventa 2 resto 0
        print(numero%2, end="")                # 2 diventa 1 resto 0, 1 diventa 0 con resto 1,  a 0 finisce la funzione, qui i print verranno fatti dall'ultima chiamata
    
    
    
    
conversione(34)
    