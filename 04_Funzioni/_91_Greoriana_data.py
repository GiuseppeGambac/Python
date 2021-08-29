def ordinamento(giorno,mese,anno):
                                     # non sto a pensare ai bisestili
    
    gennaio , marzo , maggio , luglio , agosto , ottobre , dicembre = 31,31,31,31,31,31,31
    aprile , giugno ,settembre , novembre = 30,30,30,30
    
    if mese == 1:
        return giorno
    elif mese == 2:
        return gennaio+giorno
    elif mese ==3:
        return gennaio+28+giorno
    elif mese == 4:
        return gennaio+28+marzo+giorno
    elif mese ==5:
        return gennaio+28+marzo+aprile+giorno
    elif mese ==6:
        return gennaio+28+marzo+aprile+maggio+giorno
    elif mese ==7:
        return gennaio+28+marzo+aprile+maggio+giugno+giorno
    elif mese ==8:
        return gennaio+28+marzo+aprile+maggio+giugno+luglio+giorno
    elif mese ==9:
        return gennaio+28+marzo+aprile+maggio+giugno+luglio+agosto+giorno
    elif mese ==10:
        return gennaio+28+marzo+aprile+maggio+giugno+luglio+agosto+settembre + giorno
    elif mese ==11:
        return gennaio+28+marzo+aprile+maggio+giugno+luglio+agosto+settembre +ottobre + giorno
    elif mese ==12:
        return gennaio+28+marzo+aprile+maggio+giugno+luglio+agosto+settembre +ottobre + novembre + giorno
    
    
    
if __name__ == '__main__':   
    
    print(ordinamento(2,7,2020))
