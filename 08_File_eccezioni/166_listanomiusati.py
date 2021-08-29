
dizionariomaschi = []
dizionariofemmine = []
numeroiniziale = 1900

while numeroiniziale != 2003:
    path = "C:\\Users\\Faventia Automation\\Desktop\\Programmazione\\VScode\\Python\\BabyNames\\"
    nomefile = str(numeroiniziale) +"_BoysNames.txt"

    file = open(path  + nomefile, "r")

    for linee in file:
        primariga =file.readline()
        listariga = primariga.split()
   
        if listariga[0] not in dizionariomaschi:
         dizionariomaschi.append(listariga[0])
    
      
    file.close()

    nomefile = str(numeroiniziale) +"_GirlsNames.txt"

    file = open(path + nomefile, "r")

    for linee2 in file:
        primariga =file.readline()
        listariga = primariga.split()

        if listariga[0] not in dizionariofemmine:
         dizionariofemmine.append(listariga[0])
       
    
    file.close()
    
    numeroiniziale +=1




print(dizionariomaschi)
print(dizionariofemmine)