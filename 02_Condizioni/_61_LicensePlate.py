print("Inserisci la targa")


targa = str(input())




if len(targa) == 6 or len(targa) == 8:
    
    if targa[0].isalpha() and targa[1].isalpha() and targa[2].isalpha() and targa[3].isdigit() and targa[4].isdigit() and targa[5].isdigit():
        print("è vecchia")
    elif targa[0].isdigit() and targa[1].isdigit() and targa[2].isdigit() and targa[3].isdigit() and targa[4].isalpha() and targa[5].isalpha() and targa[6].isalpha() and targa[7].isalpha():
        print("è nuova")
    else:
        print("è sbagliata")
    
else:
    print("targa non valida")








