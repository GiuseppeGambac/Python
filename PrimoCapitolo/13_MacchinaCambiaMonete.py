print("Soldi iniziali")
numero1 = round(float(input()),3)                                                                  # HO SITEMATO COSI, ARROTONDO IL FLOAT A 3 DECIMALI


Monete50 = 0.50
Monete20 = 0.20
Monete10 = 0.10
Monete5 = 0.05
Monete2  = 0.02                                                                                      # Perdo qualche valore nlle virgole e il programma non funziona
Monete1 = 0.01

numeroda50 = int(numero1 / Monete50)

Conteggiorimanente =  (numero1 - (numeroda50 * Monete50)) 


numeroda20 = int(Conteggiorimanente / Monete20) 

Conteggiorimanente = Conteggiorimanente - (numeroda20 * Monete20)

numeroda10 = int(Conteggiorimanente / Monete10  )

Conteggiorimanente = Conteggiorimanente - (numeroda10 * Monete10)


numeroda1    = int(Conteggiorimanente  / Monete1  )

print(str(numeroda50) + " 50 centesimi")
print(str(numeroda20) + " 20 centesimi")
print(str(numeroda10) + " 10 centesimi")
print(str(numeroda1) + " 1 centesimi")




