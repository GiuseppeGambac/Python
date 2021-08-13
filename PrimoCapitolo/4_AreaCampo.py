print("inserisci larghezza del campo in metri")
larghezza = float(input())
print("inserisci lunghezza del campo in metri")
lunghezza = float(input())

areacampo = larghezza * lunghezza

areacampo_acri = areacampo * 0.000247105

print(str(areacampo_acri) + " Acri")