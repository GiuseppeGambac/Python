import _125_Mescolamazzo

def Mano(numeromani,numerocarte,mazzo):
    
    totalecarte = numeromani + numerocarte
    mani = [[],[],[],[]]
    
    while len(mani[3]) != numerocarte: 
     for i in range(numeromani):
        mani[i].append(mazzo[0])
        mazzo.pop(0)
        
    return mani
        
        
        
        
        
        
        
    

mazzo = _125_Mescolamazzo.mescolamazzo(_125_Mescolamazzo.definizionemazzo())


print(Mano(4,5,mazzo))


