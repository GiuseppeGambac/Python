

perimetro = 0.0

while True:
    print("inserisci due punti")
    x = input()
    
    if not x:
        break
    
    
    y = input()
    
    lunghezza = float(y) - float(x)
    perimetro += lunghezza
    
    
print(perimetro)

    
