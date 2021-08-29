mese = input("metti il nome del mese: ")

giorno = int(input("metti il numero del giorno: "))


if mese == "dicembre": 
  if giorno >= 22:
        print("capricorno")
  else:
        print("saggitario")
elif mese == "gennaio":
    if giorno <= 19:
        print("capricorno")
    else:
        print("acquario")
elif mese == "febbraio":
    if giorno <= 18:
        print("acquario")
    else:
        print("pesci")
elif mese == "marzo":
    if giorno <= 20:
        print("pesci")
    else:
        print("ariete")
elif mese == "aprile":
    if giorno <= 20:
        print("ariete")
    else:
        print("toro")      
elif mese == "maggio":
    if giorno <= 20:
        print("toro")
    else:
        print("gemini")
elif mese == "giugno":
    if giorno <= 20:
        print("gemelli")
    else:
        print("cancro")
elif mese == "luglio":
    if giorno <= 22:
        print("cancro")
    else:
        print("leone")
elif mese == "agosto":
    if giorno <= 22:
        print("leone")
    else:
        print("vergine")
elif mese == "settembre":
    if giorno <= 22:
        print("vergine")
    else:
        print("libra")
elif mese == "ottobre":
    if giorno <= 22:
        print("libra")
    else:
        print("scoprione")
elif mese == "novembre":
    if giorno <= 21:
        print("scorpione")
    else:
        print("saggitario")
        
        
