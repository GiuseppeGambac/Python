def controllo(lato1,lato2,lato3):
    
    if lato1 + lato2 <= lato3:
        return False
    elif lato2 + lato3 <= lato1:
        return False
    elif lato3 + lato1 <= lato2:
        return False
    else:
        return True
    
    
    
print(controllo(4,1,6))
print(controllo(4,3,6))