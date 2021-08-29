import math

altezza = float(input("inserisci altezza cilindro:"))
raggio = float(input("inserisci raggio cilindro:"))



base = raggio*raggio*math.pi

volume = base * altezza

print(volume)