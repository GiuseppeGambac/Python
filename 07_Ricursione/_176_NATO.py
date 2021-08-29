def Spelling(parola):
    frase =""
    dizionario = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'I':'India', 'J':'Juliet', 'K':'Kilo', 'L':'Lima',
                   'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey',
                   'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}
    
    
    if len(parola) == 1 :
         frase  += dizionario[parola[0]]         # se la parola ha un sol carattere lo aggiungo e termino la funzione
         return frase
    
    
    if parola[0] in dizionario:                   # aggiungo il valore del primo carattere alla parola finale
        frase += dizionario[parola[0]]
        
    if len(parola) > 0  :                        # se la parola ha più di un carattere lancio la funziona eliminando la prima lettera e così via
     frase += Spelling(parola[1:])
    
        
    
        
    
    
    return frase




print(Spelling("ABCPQ"))