def token (stringa):
   stringanumeri =""
   lista =[]
   simboli = "+-*/^()"
   numero = False
   
   
        
   for i in range(len(stringa)): 
       
     if numero and not stringa[i].isnumeric():  
        lista.append(stringanumeri)
        stringanumeri=""
        numero =False
     
     
     if stringa[i] in simboli:
         lista.append(stringa[i])
         continue
     
     if stringa[i].isnumeric():
         stringanumeri += stringa[i]
         numero = True
     
              
         
         
         
   return lista





print(token("(123)+(34)"))
         
    
    