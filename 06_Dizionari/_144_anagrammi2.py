def Anagramma (stringa,stringa2):
    
    
    
    dizionario ={}
    anagrammabool = False
    
    
    for i in range(len(stringa)):
        
      if stringa[i].isalpha():  
        dizionario[i] = stringa[i]
        
        
    for x in range((len(stringa2))):
      if stringa2[x].isalpha():
        if stringa2[x] in dizionario.values():
            anagrammabool = True
        else: 
            return False
      
   
            
        
    return anagrammabool


print(Anagramma("william shakespeare","i am a weakish speller"))