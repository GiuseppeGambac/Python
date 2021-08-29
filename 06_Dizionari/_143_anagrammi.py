def Anagramma (stringa,stringa2):
    
    if len(stringa) != len(stringa2):
        return "errore lunghezza"
    
    
    dizionario ={}
    anagrammabool = False
    for i in range(len(stringa)):
        dizionario[i] = stringa[i]
        
        
    for x in range((len(stringa2))):
        if stringa2[x] in dizionario.values():
            anagrammabool = True
        else: 
            return False
      
   
            
        
    return anagrammabool
    
    
if __name__ == '__main__':    
 print(Anagramma("ciao","coia"))