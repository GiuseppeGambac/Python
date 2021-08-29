
# Divisione che arrotonda

minuti = 105
OreFilm = minuti // 60   # è il contrario del modulo
print(OreFilm)

# Divisione che da il Modulo

minuti2 = 105
MinutiDopoOra = minuti2 % 60
print(MinutiDopoOra)



# ==
# !=
# < >
# <= >=

# and - or - not
# if elif else


def compara (x,y):      # Funzione che riporta un valore all'esterno 
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1

print(compara(10, 11))           