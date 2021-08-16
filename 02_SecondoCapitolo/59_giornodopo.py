print("inserisci l'anno")
anno = int(input())
print("inserisci il mese")
mese = int(input())
print("Inserisci il giorno")
giorno =int(input())


def resto(x,y):

    restofunzione = x -(int((x/y))*y)
    return restofunzione


errore = False

if mese > 12 or mese < 0:                  # controllo se i numeri sono ok
    print("errore mese")
    errore = True

if giorno > 31 or giorno < 0:
    print("errore giorno")
    errore = True

if not errore:

    giorno += 1

    if mese == 1 or mese == 3 or mese == 5 or mese == 7 or mese == 8 or mese == 10 or mese == 12:
        if giorno > 31:                     # se in questi mesi il giorno supera il 31 vuol dire che cambio mese e torno al primo giorno
            mese += 1
            giorno= 1
    else:
       if mese != 2:                      # se non è febbraio
        if giorno > 30:      
            mese += 1
            giorno=13
       else:                              # se è febbario, dovrei capire se è un anno bisestile o no
         """
            if resto(anno,4) == 0 or resto(anno, 400) == 0 :  sbagliato    #anno bisestile, se è divisibile per 4 oppure è divisibile per 400, 

                    if giorno > 29:
                        mese+=1                   #Febbraio  
                        giorno =1   
            else:
                    if giorno > 28:
                        mese+=1                   #Febbraio  non bisestile
                        giorno =1      
         """



    if mese > 12:                      # se arrivo al 13 vuol dire che ho passato l'anno
        mese = 1
        anno +=1 

    print(anno)
    print(mese)
    print(giorno)





