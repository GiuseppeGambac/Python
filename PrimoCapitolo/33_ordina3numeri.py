numero = [0,0,0]
for i in range (3):
   
 print("inserisci 3 numeri")
 numero[i] =  int(input())


minimo = min(numero[0],numero[1],numero[2])
massimo =max(numero[0],numero[1],numero[2])


medio = (numero[0]+numero[1] + numero[2]) - (minimo + massimo)   # così trovo il medio


print(minimo)
print(medio)
print(massimo)