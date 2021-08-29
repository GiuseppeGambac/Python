

def Rotazioneparole(parola,numerosalto):
   nuovaparola = ""                                     # creo una stringa
   lunghezzaparola = len(parola)

   for i in range(lunghezzaparola):

     nuovalettera = chr(ord(parola[i]) + numerosalto)
     nuovaparola += nuovalettera                               #aggiungo ogni carattere alla stringa

   return nuovaparola
        

  

print(Rotazioneparole('cheer', 7))  

        




fin = open('FileDaleggere.txt')
"""
print(fin.readline())               # coì posso leggere il contenuto del file riga per riga 
print(fin.readline())
"""
"""
for linee in fin:                     # cosi posso stampare tutte le righe di un file txt
    word = linee.strip()
    print(word)
"""


for linee in fin:                    ## stampo solo le stringhe che sono lunghe di piu di 20 caratteri
    word = linee.strip()            

    if len(word) >= 20:
        print(word)


filetesto2 = open('FileDaleggere.txt')      # esercizio da finire, è il 9.2...il programma continua a stampare l'ultima frase 

for linea in filetesto2:
    word = linea.strip()
   
    for i in range(len(word)):
      UltimaParola = ''
      if word[i] == 'a' and UltimaParola != word:
          UltimaParola = word
          print(word)
