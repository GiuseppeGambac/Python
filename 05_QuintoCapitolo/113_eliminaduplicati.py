

stringa = input()
lista = []

while stringa != "":
    
    if not stringa in lista:        # controllo che non esista
    
     lista.append(stringa)
    stringa = input()
    
    
    




for i in range(len(lista)):
    print(lista[i])