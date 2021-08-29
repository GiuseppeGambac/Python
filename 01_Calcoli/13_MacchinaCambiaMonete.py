

print("Soldi iniziali")

numero1 = round(float(input()),2)   # comando per arrotondare a due numeri dopo la virgola                                                               # HO SITEMATO COSI, ARROTONDO IL FLOAT A 3 DECIMALI


Monete50 = 0.50
Monete20 = 0.20
Monete10 = 0.10
Monete5 = 0.05
Monete2  = 0.02                                                                                      # Perdo qualche valore nlle virgole e il programma non funziona
Monete1 = 0.01




numeroda50 = numero1 // Monete50

Conteggiorimanente =  round(numero1 % Monete50,2)    # non arrotondo a 0 ma tengo due cifre dopo la virgola


numeroda20 = Conteggiorimanente // Monete20

Conteggiorimanente = round(Conteggiorimanente % Monete20,2)

numeroda10 = Conteggiorimanente // Monete10

Conteggiorimanente = round(Conteggiorimanente % Monete10,2)


numeroda1    = Conteggiorimanente // Monete1

print(numeroda50 + " 50 centesimi")
print(numeroda20 + " 20 centesimi")
print(numeroda10 + " 10 centesimi")
print(numeroda1 + " 1 centesimi")




