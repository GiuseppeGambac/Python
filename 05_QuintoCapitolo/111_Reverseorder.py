lista =[]
numero =int(input())

while numero!=0:
    
    lista.append(numero)
    numero = int(input())
    
lista.reverse()           #Inverte la lista, l'ultimo diventa il primo ecc

for i in range(len(lista)):
 print(lista[i]) 