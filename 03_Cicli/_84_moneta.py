import random

conteggioH = 0
conteggioT = 0
conteggio = 0
while conteggioH !=3 and conteggioT != 3:
     moneta = random.randrange(1,3)
     
     if moneta == 1:
         print("H")
         conteggioH = conteggioH + 1
         conteggioT = 0
        
         
     elif moneta ==2:
         print("T")
         confronto = False
         conteggioT = conteggioT +1
         conteggioH = 0
         
         
     conteggio += 1
     
     
print(conteggio)
         
          
     
