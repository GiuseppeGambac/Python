
i = 0
totalepunteggio = 0.0

print("inserisci il voto")
lettera = input()

while lettera  != "":

    
    if lettera == "f":
        punteggio = 0.0
    elif lettera == "d":
        punteggio = 1.0
    elif lettera == "d+":
        punteggio = 1.3
    elif lettera == "c-":
        punteggio =1.7
    elif lettera =="c":
        punteggio = 2.0
    elif lettera == "c+":
        punteggio =2.3
    elif lettera == "b-":
        punteggio =2.7
    elif lettera =="b":
        punteggio = 3.0
    elif lettera == "b+":
        punteggio =3.3
    elif lettera == "a-":
        punteggio =3.7
    elif lettera =="a":
        punteggio = 4.0
    elif lettera == "a+":
        punteggio =4.3
        
                  
    
    i += 1
    totalepunteggio += punteggio
    print("inserisci il voto")
    lettera = input()
    
    
    
    
media = totalepunteggio / i
print(media)
    