import random

def lanciodadi():
    dado1 = random.randint(1,6) 
    dado2 = random.randint(1,6)
    
    return dado1 + dado2


dizionario = { }
for i in range(999):
    
    numero = lanciodadi()
    
    if  not numero  in dizionario:
        dizionario[numero] = [1,1]             # alla chiave numero metto dentro una lista
    else:
        dizionario[numero][0] += 1             # sommo il primo elemento della lista
        
        
   
        
for x in dizionario:
    dizionario[x][0] =dizionario[x][0] / 10     # lo rendo in percentuale
    
   
print(dizionario)
    
