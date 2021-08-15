import math

print("inserisci i primi due punti")

t1 = math.radians(float(input()))
g1 = math.radians(float(input()))

print("inserisci i secondi due punti")

t2 = math.radians(float(input()))
g2 = math.radians(float(input()))


distanza = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2)*math.cos(g1-g2))

print(distanza)