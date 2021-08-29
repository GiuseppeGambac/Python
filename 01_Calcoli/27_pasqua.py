anno = int((input("inserisci un anno:")))



a = anno % 19
b = anno // 100
c = anno % 100
d = b // 4
e = b / 4
f = (b+8) // 25
g = (b-f+1) // 3
h = (19*a +b -d -g +15) % 30
i = c // 4
k = c % 4
l = (32 + 2*e +2*i -h - k) % 70
m = (a + 11*h + 22*l) / 451

mese = (h +1 -7*m + 114) // 31

giorno = 1+ (h+l-7*m+114) / 31

print(giorno)
print(mese)