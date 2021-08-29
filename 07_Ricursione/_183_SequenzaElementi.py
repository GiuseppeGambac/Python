def controllo(parola,dizionario):
    somma =parola
   
    lunghezza = len(parola) -1
    
       
    
    if not parola[lunghezza] in dizionario:             # se la parola non è nel dizionario spezzo la sequenza
         return parola
     
     
    if parola[lunghezza] in dizionario:                  # se la parola è nel dizionario, salvo la parola e la rimuovo dal dizionario
           ultimaparola = dizionario[parola[lunghezza]]            
           del dizionario[parola[lunghezza]]
           somma += controllo(ultimaparola,dizionario)   # parola era = a somma quindi aggiungo un'altra parola a somma e così via
           return somma
   
    
    
dizionario = {"a":"Actinium","b":"Boron",
                "c":"Carbon","d":"Dubnium",
                "e":"Erbium","f":"Fluorine","g":"Gallium","h":"Hydrogen","i":"Iodine",
                "k":"Potassium","l":"Lanthanum","m":"Moscovium",
                "n":"Nitrogen","o":"Oxygen",
                "r":"Radium",
                "s":"Sulfur",

                
                "u":"Uranium",
                "v":"Vanadium","w":"Tungsten","x":"Xenon","y":"Yttrium",
                "z":"Zinc"}    
    
    
print(controllo("molybdew",dizionario))

print(controllo("magnesius",dizionario))