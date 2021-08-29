import turtle

turtle1 = turtle.Turtle()

def Quadrato(t,lunghezza):           #creo una funzione per fare un quadrato
   for i in range (4):
       t.lt(90)                      # giro l'angolo
       t.fd(lunghezza)


Quadrato(turtle1,200)      

   


def poligono(t,n,lunghezza):        # faccio un'altra funzione
    angolo = 360/ n
    for i in range (n):
        t.fd(lunghezza)
        t.lt(angolo)
        
        
poligono(turtle1,7,70)



def cerchio(t,r):
    circonferenza = 2* 2*(3.14) * r
    n = 50
    lunghezza = circonferenza / n
    poligono(t,n,lunghezza)           


if __name__ == '__main__':
 cerchio(turtle1,10)
