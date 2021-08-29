


parola =input()



dizionario = {}

for i in range(len(parola)):
    if not parola[i] in dizionario:
        dizionario[parola[i]] =[parola[i]] 
    
    
    
print(dizionario)