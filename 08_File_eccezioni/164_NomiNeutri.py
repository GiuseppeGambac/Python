
listamaschi = []
listafemmine = []

numeroiniziale = input()

try:
    
    path = "C:\\Users\\Faventia Automation\\Desktop\\Programmazione\\VScode\\Python\\BabyNames\\"
    nomefile = str(numeroiniziale) +"_BoysNames.txt"

    file = open(path  + nomefile, "r")

    for linee in file:
        primariga =file.readline()
        listariga = primariga.split()

        if listariga[0] not in listamaschi:
         listamaschi.append(listariga[0])
        
    file.close()

    nomefile = str(numeroiniziale) +"_GirlsNames.txt"

    file = open(path + nomefile, "r")

    for linne in file:
        primariga =file.readline()
        listariga = primariga.split()

        if listariga[0] not in listafemmine:
         listafemmine.append(listariga[0])
    
    file.close()
except:
    print("file non trovato")  

listacomuni =[]
for x in range(len(listamaschi)):
  if  listamaschi[x] in listafemmine:
      listacomuni.append(listamaschi[x])
      

print(listafemmine)
print(listamaschi)      
print(listacomuni)
