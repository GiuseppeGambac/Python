class Time():
    
    
    ore = 0
    minuti = 0
    secondi = 0
    
    def Stampatempo(self):                                                 # self è la parola standard per far riferimento a se stessa
        print('%d:%d:%d' %(self.ore ,self.minuti ,self.secondi))
    
    
class Time2():
    
    def __init__(self,ore,minuti,secondi=0):                    # creo una classe uguale, ma a sto giro creo il costruttore, in questo modo quando
                                                         # richiamerò la funzione dovrò inserire questi parametri, se inposto un valore quel valore non sarà necessario in input
     self.ore = ore
     self.minuti =minuti
     self.secondi = secondi
    
    def __str__(self):                                                       # con questo metodo quando farò print(funzione) decido cosa mostrare al posto dell'area di memoria
        return '%d:%d:%d' %(self.ore ,self.minuti ,self.secondi)
        
    

    def __add__(self,other):                                       # con questo oggetto posso creare un tipo di operazione fra questa classe e un altra classe, ad esempio
      if isinstance(other,Time):                                   # una somma di valori. con isisinstance posso capire che tipo di operandi sto usando e in base a quello scelgo cosa fare
        altreore = self.ore + other.ore                            
        return altreore
      else:
        altreore = self.ore + other
        return altreore
    
      
orario = Time()
orario.ore   = 8
orario.minuti  = 56
orario.secondi = 32

orario.Stampatempo()



orario2 = Time2(3,10)     # non metto i secondi
orario3 =Time2(1,11)

print(orario2 + orario3)       # ho creato una somma fra questi due valori
## print(orario3 + 5)          # il problema è che ormai ho usato il primo tipo di add e adesso userà solo quello, se commento la linea sopra invece userà sempre un intero


        