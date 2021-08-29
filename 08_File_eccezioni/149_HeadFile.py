import os




try:
    
    
    
    nomefile = input()
    file =   open(nomefile , "r")
except:
    print("file non trovato")
    quit()
    
     
for i in range(10):    
 print(file.readline())   # così leggo 10 volte la linea successiva
 
 
 
  
print(file.readlines())  # cos' mi crea una lista con tutte le linee


file.close()   # chiudo il file
