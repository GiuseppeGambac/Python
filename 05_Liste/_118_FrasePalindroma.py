def soloparole(stringa):
    
 parola = stringa.split()
 return parola






frase = input()


frasespezzata = soloparole(frase)

frasealcontrario = frasespezzata.copy()
frasealcontrario.reverse()

if frasespezzata == frasealcontrario:
    print("palindroma")
else:
    print("no palindroma")
