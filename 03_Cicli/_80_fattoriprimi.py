print("inserisci un numero")

n = int(input())

factor = 2


if n < 2:
    print("errore")
else:
    while factor <= n:
        if n % factor ==0:
            print("fine")
            print(n//factor)
            break
        else:
            factor += 1