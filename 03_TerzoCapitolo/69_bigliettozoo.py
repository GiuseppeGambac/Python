
prezzototale =0.0
while True:
    
    print("inserisci l'età")
    
    etastringa = input()
    
    if not etastringa:
        break
    
    eta = int(etastringa)
    
    if eta >= 3 and eta <=12:
        prezzototale += 14
    elif eta > 12 and eta <65:
        prezzototale += 23
    elif eta >= 65:
        prezzototale +=18
        
        
        
print(prezzototale)