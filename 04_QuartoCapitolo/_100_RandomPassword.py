import random

def RandomPassword():
    
    lunghezza = random.randint(7,11)
    parola=""
    for i in range(lunghezza):
        lettera = chr(random.randint(48,122))
        parola += lettera
        
    return parola


if __name__ == '__main__':

    print(RandomPassword())