import random



trovato = False
while not trovato:
    nomefile = input()
    try:
        file = open(nomefile, "r")
        trovato = True
    except:
        print("nome sbagliato")
        

listaparole = file.readlines()          #metto tutte le parole in una lista
password =""


while  len(password) > 10 or len(password) < 8:
    random1= (random.randint(0,len(listaparole) -1))          #prendo due parole random
    random2 = (random.randint(0,len(listaparole) -1))
    lunghezza1 = len(listaparole[random1]) -2                 # lunghezza per togliere \n
    lunghezza2 = len(listaparole[random2]) -2
    parola1 = listaparole[random1][:lunghezza1]                # parola random senza /n
    parola2 = listaparole[random2][:lunghezza2] 
    
    parola1[0].upper()
    parola2[0].upper()
    password = parola1 + parola2
    
    
print(password)
file.close()
    