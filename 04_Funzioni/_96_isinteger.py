def FindInteger(stringa):
     parola = stringa.strip()   # elimino tutt gli spazi
     for i in range(len(parola) -1):
        if parola[i].isdigit() or parola[0] == "+" or parola[0] == "-":
            numero = True
        else:
            numero = False
            break
            
     return numero




print(FindInteger("23456"))
print(FindInteger("23456         "))
print(FindInteger("2324ci256"))