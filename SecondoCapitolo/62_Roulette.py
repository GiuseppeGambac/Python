
import random

numero = random.randrange(0,40)

print("il numero è " + str(numero))

if numero > 0 and numero < 37:
  

    if (numero == 1 or numero == 3 or numero == 5 or numero == 7 or numero == 9 or numero == 12 or numero == 14 or numero == 16 or numero == 18 or numero == 19 
    or numero == 21 or numero == 23 or numero == 25 or numero == 27 or numero == 30 or  numero == 32 or numero == 34 or numero == 36):
        print("pay " + str(numero))
        print("red")
    else:
        print("pay " + str(numero))
        print("black")



    resto = numero - (int((numero /2))*2)  

    if resto == 0:
         print("odd")
    else:
         print("even")    

    if numero >0 and numero <= 18:
        print("1..18")
    else:
        print("19..36")    



elif numero == 0:
    print("pay 0")
elif numero ==00:
     print("pay 00")  

else:
    print("errore")        


