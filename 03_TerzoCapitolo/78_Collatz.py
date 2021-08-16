print("inserisci un numero")

x = int(input())


while not x == 1:
    if x % 2 == 0:
      x =  x//2
    else:
        x = x*3 +1
        
    print(x)
        
        
    