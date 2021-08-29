def centrastringa(s,w):
    if w < len(s):
        return s
    else:
        spazi = (w-len(s)) // 2
        return  "  " * spazi + s
    
    
    
    
print(centrastringa("ciao",70))