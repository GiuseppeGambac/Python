
pressure = float(input("inserisci pressione:"))
volume = float(input("inserisci volume:"))
temperatura = float(input("inserisci temperatura:"))

costantegas = 8.314

n = (pressure*volume)  / temperatura * costantegas


print(n)
