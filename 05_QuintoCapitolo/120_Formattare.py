def formatta(listastringa):
 parola=""
 for i in range(len(listastringa)-2):
     
    parola += listastringa[i] + ", "
 
 parola += listastringa[len(listastringa)-2] + " and " + listastringa[len(listastringa)-1]
 return parola
 
 
 
 
 
lista =[]
parola = input()


while parola != "":
    lista.append(parola)
    parola = input()
    
 
 
print(formatta(lista))
    
 