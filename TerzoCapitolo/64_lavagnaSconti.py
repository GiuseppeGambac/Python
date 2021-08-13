 
sconto1 = 4.95
sconto2 = 9.95
sconto3 = 14.95
sconto4 = 19.95
sconto5 = 24.95

PrezziScontati = [sconto1,sconto2,sconto3,sconto4,sconto5]    # Lo uso anche se non è ancoa stato spiegato....

for i in range(5):
    prezzoNoSconto = (PrezziScontati [i] * 100) / 40
    print(str(PrezziScontati[i]) + "e il prezzo normale sarebbe " + str(prezzoNoSconto))

