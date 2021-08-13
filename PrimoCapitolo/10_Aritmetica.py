import math

print("numero A")
numeroA = int(input())


print("numero B")
numeroB = int(input())



print(str(numeroA + numeroB))
print(str(numeroA - numeroB))
print(str(numeroA * numeroB))
print(str(numeroA / numeroB))

Resto =  numeroA -  (int(numeroA / numeroB) * numeroB)   # si calcola così il resto
print(str(Resto))

print(str(math.log10(numeroA)))
print(str(numeroA**numeroB))            # Potenza2