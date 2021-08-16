def NumeroPrimo(numero):
    
    if numero % 2 == 0:
        primo = False
    else:
     for i in range(2,numero):
        if numero % i == 0:
            primo = False
            break
            
        else:
            primo = True
    return primo

        
        
if __name__  == '__main__':       
 
    print(NumeroPrimo(7))
    print(NumeroPrimo(9))
    print(NumeroPrimo(11))
    print(NumeroPrimo(15))

