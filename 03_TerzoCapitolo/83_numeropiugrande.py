import random

x = random.randrange(1,100)
conteggio = 0
max = x

for i in range (100):
    y = random.randrange(1,100)
    
    if y > max:
        max = y
        print("%d <== update" %max)
        conteggio = conteggio + 1


print(conteggio)