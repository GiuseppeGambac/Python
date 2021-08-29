anno = int(input())



giorno = (anno + ((anno-1) //4 ) -  ((anno-1) //100 ) +   ((anno-1) //400 )) % 7


if giorno ==1:
    print("lunedi")
elif giorno == 2:
    print("martedi")
elif giorno == 3:
    print("mercoledi")
elif giorno == 4:
    print("giovedi")
elif giorno == 5:
    print("venerdi")
elif giorno == 6:
    print("sabato")
elif giorno == 7:
    print("domenica")