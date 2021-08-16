import math


print("Metti il primo lato del triangolo")
lato1 = int(input())

print("Metti il secondo lato del triangolo")
lato2 = int(input())

print("Metti il terzo lato del triangolo")
lato3 = int(input())

diametro = lato1 + lato2 + lato3 
AreaTriangolo = math.sqrt(diametro * (diametro - lato1)*(diametro-lato2)*(diametro-lato3))

print(AreaTriangolo)
