def riduci (numero):
    
    a = 1
    b = 3*a
    c = 16*b                                     # ho capito male l'esercizio.....
    
    conteggioa = 0
    conteggiob = 0
    conteggioc = 0
    
    
    
    while numero >= c :
      
      numero =   numero - c
      conteggioc +=1
    
    while numero >= b:
      print(numero)
      numero = numero - b
      conteggiob +=1    
      
    while numero >= a:
      numero -= a
      conteggioa += 1
        
    return conteggioc,conteggiob,conteggioa


print(riduci(301))
    