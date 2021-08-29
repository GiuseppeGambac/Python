def Giornimese(mese,anno):
    bisestile = False
    if mese < 1 or mese > 12 :
        return "error"
    
    if anno % 400 == 0:
        bisestile = True
    elif anno % 100 == 0:
        bisestile = False
    elif anno % 100 != 0:
        if anno % 4 ==0:
         bisestile = True
    else:
        bisestile = False    
        
        
        
    if mese == 1 or mese == 3 or mese == 5 or mese == 7 or mese == 8 or mese == 10 or mese == 12:
        return 31
    else:
       if mese != 2:                      # se non è febbraio
          return 30
       else:
        if bisestile:
            return 29
        else:
            return 28
        
        
        
if __name__ == '__main__':       
    print(Giornimese(2,2020))
    

     
     
     
    
    
    