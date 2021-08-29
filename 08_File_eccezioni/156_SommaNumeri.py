
somma = 0

cifra = input()                        # prendo il numero come stringa
 
while cifra != "":              
  try:   
      
     somma += int(cifra)               # ne faccio la somma  
     print(somma)
     
  except :
      print("metti un numero")         # se la conversione in numero non funziona lancio un warning e vado avanti con il programma,metto un input e ricomincio il while
      
  cifra = input()