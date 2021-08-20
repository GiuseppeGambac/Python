
input_ =input()
negativi = []
zero = []
positivi = []


while input_ != "":
    
    numero = int(input_)
    
    if numero < 0:
        negativi.append(numero)
    elif numero > 0:
        positivi.append(numero)
    else:
        zero.append(numero)
    

    input_=input()
    
    
lista = negativi + zero + positivi
    
print(lista)