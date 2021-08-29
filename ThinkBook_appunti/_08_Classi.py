import copy

class Point:
    """ci sono due punti nello spazio"""   # se metto questo commento poi tramite help(nomefunzione) posso vedere come funziona, oppure se ci passo sopra mi fa leggere il commento
    x =0
    y = 0
 
 
def Distanza(p1,p2):
    punto =Point()
    punto.x = p2.x -p1.x
    punto.y = p2.y -p1.y
    return punto.x,punto.y

def Modificapunto(p):
   p.y = 35
   
   
class Rettangolo():
      altezza = 0.0
      larghezza = 0.0
      angoli = Point()  # può contenere un'altra classe
        

    




punto1 =Point()
punto2 =Point()



punto1.x = 10
punto1.y = 5
punto2.x =20
punto2.y =10

print("distanza")
print(Distanza(punto1,punto2))
#################################################
Modificapunto(punto2)
print("modifica Y")
print(punto2.y)                   # se metto una classe in uno oggetto viene modificata come un dizionario o una lista


punto3 = copy.copy(punto1)   # in questo modo copio e non punto allo stesso contenitore

punto3.x=50
print("Copy")
print(punto1.x)

####################################################


rettangolo1 =Rettangolo()

rettangolo1.larghezza =100
rettangolo1.altezza   = 200
rettangolo1.angoli.x  = 10
rettangolo1.angoli.y  =20


rettangolo2 = copy.deepcopy(rettangolo1)    # deep copy copia anche le classi interne 
rettangolo2.altezza=500
rettangolo2.angoli.x =50
print("modifica rettangolo")
print(rettangolo2.larghezza)
print(rettangolo2.altezza)
print(rettangolo2.angoli.x)
print(rettangolo2.angoli.y)
print("controllo punto dell'altro rettangolo")
print(rettangolo1.angoli.x)                      # ho cambiato anche l'istanza dell'angolo del primo rettangolo, per evitare ciò devo usare deepcopy
