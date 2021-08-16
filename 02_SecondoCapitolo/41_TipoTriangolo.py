print("inserisci i tre lati")
lato1 = float(input())
lato2 = float(input())
lato3 = float(input())

if lato1 == lato2 and lato2 == lato3:
    print("triangolo equilatero")
elif (lato1 == lato2 and lato2 != lato3) or (lato2 == lato3 and lato3 != lato1) or (lato3 == lato1 and lato3 != lato2)  :
    print("triangolo isoscele")
else:
    print("triangolo scaleno")    
    
    