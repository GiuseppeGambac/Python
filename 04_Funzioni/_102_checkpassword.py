def Controllopassword(stringa):
    lunghezza = len(stringa)
    
    errore = False
    if lunghezza < 8:
        errore = False
    else:
        primocontrollo =False
        secondocontrollo = False
        
        for i in range(lunghezza-1):
            if stringa[i].isupper():
                primocontrollo = True
                
        if primocontrollo:         
            for i in range(lunghezza-1):
                if stringa[i].islower():
                    secondocontrollo = True
                    
        if secondocontrollo:        
            for i in range(lunghezza-1):
                if stringa[i].isdigit():
                    errore = True
    
    
    return errore





if __name__ == '__main__':
    print(Controllopassword("ciao"))
    print(Controllopassword("ciaoooooo"))
    print(Controllopassword("Ciaooo234"))