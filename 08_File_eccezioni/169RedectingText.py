trovato = False
while not trovato:
    nomefile = input()
    try:
        file = open(nomefile, "w")
        trovato = True
    except:
        print("nome sbagliato")
        
trovato2 = False
while not trovato2:
    nomefile = input()
    try:
        file2 = open(nomefile, "r")
        trovato2 = True
    except:
        print("nome sbagliato")
        

lista =[]       
for linee in file2:
    lista.append(linee)
    
file2.close()


for linee2 in file:
    
    listaparole = linee2.split()
    
    for x in range(len(lista)):
        if lista[x] in listaparole:
            print("ciao")
            
            