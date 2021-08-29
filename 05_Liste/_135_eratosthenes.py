
numero = int(input("inserisci un numero"))

numeri = []
for i in range(0, numero + 1):
 numeri.append(i)

numeri[1] = 0

p=2
while p < numero:

  for i in range(p*2, numero + 1, p):
   numeri[i] = 0

  p=p+1
  while p < numero and numeri[p] == 0:
   p=p+1

for i in numeri:
 if numeri[i] != 0:
  print(i)