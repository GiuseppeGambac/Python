def FindInteger(stringa):
 
     for i in range(len(stringa) -1):
        if stringa[i].isdigit() or stringa[0] == "+" or stringa[0] == "-":
            numero = True
        else:
            numero = False
            break
            
     return numero




print(FindInteger("23456"))
print(FindInteger("2324ci256"))