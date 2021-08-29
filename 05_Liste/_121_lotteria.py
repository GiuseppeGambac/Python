import random


lista = []

while len(lista) < 6:
 numero =random.randint(1,49)
 if not numero in lista:
  lista.append(numero)
 
 
 
print(lista)
 