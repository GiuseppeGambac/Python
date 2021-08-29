from typing import Tuple


tuple1 = ('a' , 'b' , 'c' , 'd' , 'e')
tuple2 = 'a',                            # devo mettere la virgola finale se ho un solo elemento

print(type(tuple1))
print(type(tuple2))



stringa = "ciao"
tuple3 = tuple(stringa)            # rendo una stringa un tuple

print(tuple3)


#  tuple3[2] = "C"     # non si possono modificare

tuple3 = tuple3[0:2] + ('T',) + tuple3[3:]      # cos' possom modificarlo
print(tuple3)
 
 
 
 
a,b = (10,40)          # posso usare i tuple per assegnare più variabili velocemente

print(a)



def stampatutto(*argvs):          # con l'asterico posso inserire più valori, cioè prende un tuple
    print(argvs)
    
    
stampatutto(1,20,40,"ciao")