

cifra = float(input())
numero = round(cifra)


if numero == 0 :
    print("F")
elif numero == 1:
    print("D")
elif numero == 1.3:
    print("D+")
elif numero == 1.7:
    print("C-")
elif numero == 2.0:
    print("C")
elif numero == 2.3:
    print("C+")
elif numero == 2.7:
    print("B-")
elif numero == 3.0:
    print("B")
elif numero == 3.3:
    print("B+")
elif numero == 3.7:
    print("A-")
elif numero == 4.0:
    print("A+")
else:
    print("errore")