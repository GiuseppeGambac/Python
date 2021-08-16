def centrastringa(s,w):
    if len(s) >= len(w):
        return s
    else:
        
        return "" * ((len(s) -len(w)) //2) + s
    
    
    
    
print(centrastringa("ciao","provaa"))