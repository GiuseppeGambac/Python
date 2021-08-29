def Romano(numeroromano):
     stringa =0
     numero = 0
     dizionario = {"M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X": 10 , "V" : 5 , "I" :1}
     
     if len(numeroromano) == 1:                                  # se sono all'ultima cifra sommo e interrompo
         stringa += dizionario[numeroromano[0]]
         return stringa
     
     
     if dizionario[numeroromano[0]] < dizionario[numeroromano[1]]:                    # se il valore precedente è minore di quello dopo faccio la differenza e lo aggiungo
         numero += dizionario[numeroromano[1]] - dizionario[numeroromano[0]]          # dopo se non sono alle ultime due cifre continuo con il controllo
         if len(numeroromano) > 2:
          numero += Romano(numeroromano[2:])
         return numero                                                                    # e alla fine ritorno questo numero
         
     
     elif numeroromano[0] in dizionario:                                       # se è tutto normale invece faccio una normale somma
         stringa += dizionario[numeroromano[0]]
         
         
     stringa += Romano(numeroromano[1:])                                       #se è tutto normale faccio un semplice richiamo al valore dopo
     return stringa                                                            # ritorno normale
 
 
 
 
 
 
print(Romano("MLDXVX"))
     
     
     