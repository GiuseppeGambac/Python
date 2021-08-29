def HexaToDecimal(stringa):
    
   numero = int(stringa[0]) * 16
   
   if stringa[1] == "A":
       numero += 10
   elif stringa[1] == "B":
       numero += 11
   elif stringa[1] == "C":
       numero += 12
   elif stringa[1] == "D":
       numero += 13
   elif stringa[1] == "E":
       numero += 14
   elif stringa[1] == "F":
       numero += 15
       
   return numero

def decimalToHex(numero):
    if numero < 10:
        return numero
    else:
        if numero == 10:
            return "A"
        elif numero ==11:
            return "B"
        elif numero ==12:
            return "C"
        elif numero ==13:
            return "D"
        elif numero ==14:
            return "E"
        elif numero ==15:
            return "F"


print(HexaToDecimal("8B"))
print(decimalToHex(14))