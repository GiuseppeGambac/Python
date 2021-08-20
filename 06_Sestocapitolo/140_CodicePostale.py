dizionario = {"A" : "Newfoundland" ,"B": "Nov Scotia" , "C" : "Prince" , "E" : "New Brunswick" , "G" : "Quebec" , "H" : "Quebec" , "J" : "Quebec",  
              "K" : "Ontario", "L" : "Ontario" ,"M" : "Ontario" ,"N" : "Ontario", "P" : "Ontario" , "R" : "Manitoba" , "S" : "Saskatchewan", "T" : "alberta",
              "V " : "british columbia", "X" : "Nuvavut or Northwest Territories" , "Y" :"Yukon"}
              
              
              
              
targa = input()

if targa[0].isalpha() and targa[1].isdigit():


        if targa[0] in dizionario:
         targafinale = dizionario[targa[0]]
        
        
        if targa[1] != 0:
         targafinale += " urban"
        else:
         targafinale += " rural"
         
        print(targafinale)
        
        
         
         
         