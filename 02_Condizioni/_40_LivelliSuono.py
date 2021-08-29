print("scrivi i decibel")

decibel = int(input())


if decibel > 130:
    print("troppo alto")                                    # l'esercizio continua con gli altri casi, sono facili, amen...
elif decibel == 130:
    print("Jackhammer")
elif decibel <130 and decibel > 106:
    print("è fra jackhammer e Gas Lawnmower")
elif decibel < 40:
    print("troppo basso")




