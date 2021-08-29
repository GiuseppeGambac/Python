
nota = input("inserisci nome nota")

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

lettera = nota[0]
ottava =  nota[1]

if lettera == "C":
 frequenza = C4
elif lettera == "D":
 frequenza = D4
elif lettera == "E":
 frequenza = E4
elif lettera == "F":
 frequenza = F4
elif lettera == "G":
 frequenza = G4
elif lettera == "A":
 frequenza = A4
elif lettera == "B":
 frequenza = B4
 
 
frequenza = frequenza / 2 ** (4-ottava)
print(frequenza)