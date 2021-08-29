import random

def Cartabingo():
     dizionario ={"B" :[], "I" :[], "N" : [], "G" : [] , "O" :[]}
     x =1
     y= 15
     for i in dizionario:
         
         dizionario[i].append( random.sample( range(x,y),5) )     # sample da indietro una lista con numeri diversi 
         x += 15
         y+= 15
    
         
     return dizionario
 
 
def stampacarta(carta):
    print("B  I  N  G  O")
    
    for x in range(5):
    
        print('%d %d %d %d %d'     %(carta["B"][0][x] ,carta["I"][0][x] ,carta["N"][0][x] , carta["G"][0][x] ,carta["O"][0][x] ))
        
      
 
 
if __name__ == '__main__':
    carta = Cartabingo()
    print(carta)
         
    stampacarta(carta)