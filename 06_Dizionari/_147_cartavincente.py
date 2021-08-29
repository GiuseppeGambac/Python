import _146_CartaBingo as carta
import random

listanumeri = [0]

for i in range(1,100):
    listanumeri.append(i)


listacarte = []

for i in range(20):
    
 listacarte.append(carta.Cartabingo()) 



numero = random.randint(1,50)

for x in range(len(listacarte)):
  for z in listacarte[x]:
      for x in z:
          if numero in x
              print(numero)


