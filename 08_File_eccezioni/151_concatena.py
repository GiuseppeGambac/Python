import sys



try:
 i =1                                  # gli argomenti li devo aggiungere nel json di visualcode
 while i != 3:
  
    
    file =   open(sys.argv[i] , "r")
    
    for x in file:
     print(x)
     
    file.close()
    i += 1
    
except:
    print("file non trovato")
    quit()
    
    
    
    

    
    


    