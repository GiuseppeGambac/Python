

nomefile = input()
try:
 file = open (nomefile, "r")
except:
    print("file non esiste")
nuovofile = open("nuovofile", "w")

numero = 1
nuovalinea = [""]
for i in file:
    
    nuovalinea.append ( "%d" %numero + ": " + i )
    nuovofile.write(nuovalinea[numero])
    numero += 1
    
file.close()
nuovofile.close()
    
    
