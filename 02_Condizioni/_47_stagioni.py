mese = input("metti il nome del mese: ")

giorno = int(input("metti il numero del giorno: "))


if mese == "gennaio" or mese == "Febbraio":
 stagione = "inverno"
elif mese == "Marzo":
 if giorno < 20:
  stagione = "inverno"
 else:
  stagione = "primavera"
elif mese == "Aprile" or mese == "Maggio":
 stagione = "primavera"
elif mese == "giugno":
 if giorno < 21:
  stagione = "primavera"
 else:
  stagione = "estate"
elif mese == "luglio" or mese == "agosto":
 stagione = "estate"
elif mese == "Settembre":
 if giorno < 22:
  stagione = "estate"
 else:
  stagione = "autunno"
elif mese == "ottobre" or mese == "novembre":
 stagione = "autunno"
elif mese == "Dicembre":
 if giorno < 21:
  stagione = "autunno"
 else:
  stagione = "inverno"
  
  
print(stagione)