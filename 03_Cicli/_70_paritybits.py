riga = input("inserisci i bit:")


while riga != "":
    
    if riga.count("0") + riga.count("1") != 8 or len(riga) != 8:
        print("errore")
    else:
        uno = riga.count("1")    # conta gli uno presenti nella stringa
        
        if uno %2 == 0:
            print(0)
        else:
            print(1)
            
    riga = input("inserisci i bit")