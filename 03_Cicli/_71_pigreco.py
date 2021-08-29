
pigreco = 3.0
approssimazione = 0.0
for i in range(15):
    giro = 4*i
    approssimazione +=  (4 / (2+giro)  *(3+giro) *(4+giro)) - (4/ ((4+giro) *(5+giro)*(6+giro)))
    
    
    pigreco += approssimazione
    
    print(approssimazione)