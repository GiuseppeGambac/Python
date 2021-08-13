print("inserisci una lettera")

lettera = str(input())


if lettera == "a" or lettera =="e" or lettera =="i" or lettera == "o" or lettera == "u":
    print("la lettera è una vocale")
elif lettera == "y":
    print("può essere una vocale o una consonante")
else:
    print("è una consonante")


