print("Inserisci il prezzo totale del pranzo che si deve pagare")
prezzo = float(input())

PrezzoConIVA = (prezzo *122) / 100              # l'iva si scorpora così



Mancia = ((prezzo* 18) / 100)

PrezzoTotale = PrezzoConIVA + Mancia


print(str("%.2f" % PrezzoTotale ) + " prezzo totale")
print(str("%.2f" % PrezzoConIVA) + " IVA")
print(str("%.2f" % Mancia)+ " mancia")


