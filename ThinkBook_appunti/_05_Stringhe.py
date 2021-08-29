stringa = 'provastringa'

lettera = stringa[1]     #Prendo su solo la seconda lettera della stringa che ho dichiarato sopra 

print(lettera)




def stampaparola(parola):           #Stampo lettera per lettera la parola, prima però devo sapere la lunghezza della parola inserita 
    Lunghezza = len(parola) 
    for i in range (Lunghezza ):
        Lettera = parola[i]
        print(Lettera)
        
def stampaparola2(parola):         # altro metodo per scorrere una stringa
    for carattere in parola:
        print(carattere)


stampaparola('provastampa')
stampaparola2("ciao")



parolaintera='due parole'        #Posso selezionare anche solo parte della frase o di una parola

partedifrase = parolaintera[6:13]

stampaparola(partedifrase)


print('-----------------------------------------')    ## separo il foglio 


partedifrase = parolaintera[8:]    # in questo modo posso selezionare tutto a a destra partendo dall'8, posso mettere il numero dell'altra 
                                   # parte per selezionare dall'imizio fino all numero

stampaparola(partedifrase)



print('-----------------------------------------')    ## separo il foglio per fare la ricerca delle parole


def RicercaLettera(parola,lettera):

    for i in range(len(parola)):
        if parola[i] == lettera :
            return True
        
    return False   


print(RicercaLettera('cane', 'z'))        # Qui il valore sarà 0
print(RicercaLettera('cane', 'n'))        # qui troverà la n e il valore sarà 1



print('-----------------------------------------')    ## separo il foglio


fraseminuscolo ='provetta'

print(fraseminuscolo.upper())        # metodo per rendere tutte le lettere grandi



print(fraseminuscolo.find('u'))      # in questo modo posso trovare in che posizione si trova la lettera


print(fraseminuscolo.find('u',2))    # qui il risultato è -1, perchè gli ho detto di partire dal terzo posto e non trova la 'u'

print(fraseminuscolo.find('i',2,5))  # qui dico di cercare la i in un determinato range 




print('-----------------------------------------')    ## separo il foglio


def letteraInComune(parola1,parola2):
    lettereinparola1 = len(parola1)


    for i in range (lettereinparola1):
   
      if  parola1[i] in parola2:             ## controllo lettera per lettera se è presente nella seconda parola tramite il comando 'in'    
          print(parola1[i])

letteraInComune('banana', 'catena')         


print('-----------------------------------------')    ## separo il foglio


parola1 = "ciao come stai?"
parolanuova = "heila" + parola1[5:]            # così posso modificare una stringa, mi tocca sempre crearne un'altra
print (parolanuova)

print('-----------------------------------------')    ## separo il foglio

frase = " ciao                "
word = frase.strip()                      # rimuove tutti gli spazi vuoti e gli a capo
word2 = parolanuova.split()               # riporta una lista con tutte le parole
print(word) 
print(word2) 


print('-----------------------------------------')    ## separo il foglio

riga = "12323298749856720981121312321321111"
print(riga.count("1") )             # posso contare gli elementi in una stringa