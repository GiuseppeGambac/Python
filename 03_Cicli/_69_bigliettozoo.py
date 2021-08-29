
prezzototale =0.0
print("inserisci l'età")
    
etastringa = input()

while etastringa != "":
    

    
    eta = int(etastringa)
    
    if eta >= 3 and eta <=12:
        prezzototale += 14
    elif eta > 12 and eta <65:
        prezzototale += 23
    elif eta >= 65:
        prezzototale +=18
        
    print("inserisci l'età")
    
    etastringa = input()
    
        
        
        
print(prezzototale)