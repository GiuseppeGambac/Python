
risultatofinale = ""

print ("inserisci la parola da modificare")
parola =str(input())
print ("inserisci il numero di shift")
numero = int(input())


for i in range(len(parola)):
    
    risultato = chr(ord(parola[i]) + numero)                 # Non ho gestito la x y z 
    risultatofinale += risultato    
          
print(risultatofinale)