print("inserisci gli anni")

anni = int(input())





if anni > 2:
    annicane =(2*10.5) + (anni -2) *4       #se gli anni sono maggiori di due
    print(annicane)
elif anni > 0 and anni <= 2:                #se gli anni sono 1 o 2
    annicane = anni * 10.5
    print(annicane)
elif anni < 0:
    print("errore")




