print("metti un valore")
cifra = input()

while cifra != "":
    
    try:   
        numero = float(cifra)       
        if numero == 0 :
            print("F")
        elif numero == 1:
            print("D")
        elif numero == 1.3:
            print("D+")
        elif numero == 1.7:
            print("C-")
        elif numero == 2.0:
            print("C")
        elif numero == 2.3:
            print("C+")
        elif numero == 2.7:
            print("B-")
        elif numero == 3.0:
            print("B")
        elif numero == 3.3:
            print("B+")
        elif numero == 3.7:
            print("A-")
        elif numero == 4.0:
            print("A+")
    except:
        
        lettera = cifra
        if lettera == "F":
            print(0)
        elif lettera == "D":
            print(1.0)
        elif lettera == "D+":
            print(1.3)
        elif lettera == "C-":
            print(1.7)
        elif lettera == "C":
            print(2.0)
        elif lettera == "C+":
            print(2.3)
        elif lettera == "B-":
            print(2.7)
        elif lettera == "B":
            print(3.0)
        elif lettera == "B+":
            print(3.3)
        elif lettera == "A-":
            print(3.7)
        elif lettera == "A":
            print(4.0)
        elif lettera == "A+":
            print(4.0)
    cifra = input()
        
        
  
