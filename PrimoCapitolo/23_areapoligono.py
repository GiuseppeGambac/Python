
import math

print("inserisci la lunghezza")
lunghezza = float(input())
print("inserisci il numero dei lati")
lati = int(input())


area = (lati * lunghezza**2) / 4 * math.tan(math.pi/lati)


print(area)