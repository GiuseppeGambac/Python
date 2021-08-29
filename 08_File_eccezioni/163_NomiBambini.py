
listamaschi = []
listafemmine = []
numeroiniziale = 1900

while numeroiniziale != 2003:
    path = "C:\\Users\\Faventia Automation\\Desktop\\Programmazione\\VScode\\Python\\BabyNames\\"
    nomefile = str(numeroiniziale) +"_BoysNames.txt"

    file = open(path  + nomefile, "r")


    primariga =file.readline()
    listariga = primariga.split()

    if listariga[0] not in listamaschi:
     listamaschi.append(listariga[0])
    
    file.close()

    nomefile = str(numeroiniziale) +"_GirlsNames.txt"

    file = open(path + nomefile, "r")


    primariga =file.readline()
    listariga = primariga.split()

    if listariga[0] not in listafemmine:
     listafemmine.append(listariga[0])
    
    file.close()
    numeroiniziale +=1



print(listafemmine)
print(listamaschi)
