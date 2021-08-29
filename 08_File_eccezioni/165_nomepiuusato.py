
dizionariomaschi = {}
dizionariofemmine = {}
numeroiniziale = int(input())
numerofinale = int(input())

while numeroiniziale != numerofinale +1:
    path = "C:\\Users\\Faventia Automation\\Desktop\\Programmazione\\VScode\\Python\\BabyNames\\"
    nomefile = str(numeroiniziale) +"_BoysNames.txt"

    file = open(path  + nomefile, "r")


    primariga =file.readline()
    listariga = primariga.split()

    if listariga[0] not in dizionariomaschi:
     dizionariomaschi[listariga[0]] =1
    else:
      dizionariomaschi[listariga[0]] += 1
      
    file.close()

    nomefile = str(numeroiniziale) +"_GirlsNames.txt"

    file = open(path + nomefile, "r")


    primariga =file.readline()
    listariga = primariga.split()

    if listariga[0] not in dizionariofemmine:
     dizionariofemmine[listariga[0]] =1
    else:
     dizionariofemmine[listariga[0]] += 1 
    
    file.close()
    numeroiniziale +=1


for i in dizionariomaschi:
    if dizionariomaschi[i] == max(dizionariomaschi.values()):
        nomemaschio = i
        
for i in dizionariofemmine:
    if dizionariofemmine[i] == max(dizionariofemmine.values()):
        nomefemmina = i


print(nomemaschio)
print(nomefemmina)