import random

def GeneraTarga():
    x = random.randint(1,2)
    
    parola =""
    
    if x == 1:
     for i in range(3):
         lettera  =   chr(random.randint(65,90))
         parola   += lettera
      
     for i in range(3):
         lettera = str(random.randint(0,9))
         parola += lettera
    elif x ==2:
     for i in range(4):
         lettera  =   chr(random.randint(65,90))
         parola   += lettera
      
     for i in range(4):
         lettera = str(random.randint(0,9))
         parola += lettera
    
    return parola




print(GeneraTarga())