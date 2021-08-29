import math

a = int(input())
b = int(input())
c = int(input())



delta = math.sqrt(b**2 - 4*a*c)


if delta < 0:
    print("non esiste")
elif delta == 0:
    root = (-b + delta) / 2*a
    print(root)
else:
    root = (-b + delta) / 2*a
    root2 = (-b - delta) / 2*a
    print(root)
    print(root2)