def CalcoloTariffa(distanza):
    distanzametri = distanza * 1000
    tariffa = distanzametri / 140
    return  tariffa* 0.25 + 4.0




print(CalcoloTariffa(10))