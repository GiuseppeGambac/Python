

x = int(input())


guess = x /2


while (guess * guess) - x >= 10**-12:
    guess = (guess + x/guess)/2
    
    
print (guess)