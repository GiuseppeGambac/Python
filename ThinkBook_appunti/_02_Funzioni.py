from _04_EserciziTurtle import cerchio  as funzioni  


def stampa (stringa):                         #definisco una semplice funzione
    print(stringa)


def FalloDueVolte(Funzione, stringa):         #Creo una funzione che lancia due volte la funzione e il valore che passo
    """cosi posso spiegare cosa fa la funzione"""
    Funzione(stringa)
    Funzione(stringa)

def FalloQuattroVolte(funzione,stringa):      # creo una funzione che lancia due volte la funzione che già lancia due volta una funzione
    FalloDueVolte(funzione, stringa)
    FalloDueVolte(funzione, stringa)


FalloDueVolte(stampa,'prova')

FalloQuattroVolte(stampa, 'prova2')





# inizio esercizio libro

linea1 ='+----+----+'
linea2 ='|    |    |'

def StampaLinea(Stringa):
    print(Stringa)

def StampaQuadrato(funzione,stringa1,stringa2):
    funzione(stringa1)
    funzione(stringa2)
    funzione(stringa2)
    funzione(stringa2)
    funzione(stringa1)
    funzione(stringa2)
    funzione(stringa2)
    funzione(stringa2)
    funzione(stringa1)

StampaQuadrato(StampaLinea,linea1,linea2)




print("------------------------------------------")
 

turtleprova = funzioni.turtle.Turtle()               # ho importato le funzioni da un altro file, gli ho dato un nome mio...al'interno dell'altro file c' il controllo del main
funzioni.cerchio(turtleprova,5)                      # per non farlo ciclare
