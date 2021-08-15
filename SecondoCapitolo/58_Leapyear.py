print("inserisci un anno")

anno = int(input())

if anno % 400 == 0:
    print("is a leap year") 
elif anno % 100 == 0:
        print("no a leap year")
elif anno % 100 != 0:
    if anno % 4 ==0:
        print("is a leap year")
else:
     print("no a leap year")       
             
