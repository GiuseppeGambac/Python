import random

def definizionemazzo():
    
    valore =[2,3,4,5,6,7,8,9,"T","J","Q","K","A"]
    simbolo =["s","h","d","c"]
    mazzo =[]
    for i in range(len(valore)):
        
        for x in range(len(simbolo)):
         mazzo.append ( str(valore[i]) + simbolo[x]  )
         
         
    return mazzo


def mescolamazzo(mazzo):
    mazzo2 = []
    
    while len(mazzo2) != len(mazzo):
        
        numero = random.randint(0,len(mazzo)-1)
        if not mazzo[numero] in mazzo2:
         mazzo2.append (mazzo[numero] )
        
    return mazzo2    


if __name__ == '__main__':
    mazzoinuso = definizionemazzo()
    print(mazzoinuso)
    print(mescolamazzo(mazzoinuso))
        