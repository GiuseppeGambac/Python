def Precedenzaoperatore(stringa):
    if stringa == "+":
        return 1
    elif stringa == "-":    # potevo far el'OR ma ormai ho fatto così
        return 1
    elif stringa == "*":
        return 2
    elif stringa == "/":
        return 2
    elif stringa == "^":
        return 3
    else:
        return -1
    
    
    
print(Precedenzaoperatore("+"))