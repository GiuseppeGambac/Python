
lista =[]
numero =int(input())

while numero!=0:
    
    lista.append(numero)
    numero = int(input())
    
lista.sort()           #Ordina dal più piccolo al più grande


for i in range(len(lista)):
 print(lista[i]) 
 