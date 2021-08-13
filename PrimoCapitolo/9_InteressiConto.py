print("Soldi iniziali")
numero1 = int(input())


Dopounanno = numero1 + (numero1 *0.04)
Dopodueanni = Dopounanno + (Dopounanno * 0.04)
Dopotreanni = Dopodueanni + (Dopounanno * 0.04)


print(str("%.2f" % Dopounanno))
print(str("%.2f" % Dopodueanni))
print(str("%.2f" % Dopotreanni))