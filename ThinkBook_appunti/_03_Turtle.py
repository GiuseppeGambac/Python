import turtle

Turtle = turtle.Turtle()      #Turle diventa quella funzione
print(Turtle)


Turtle.fd(100)                # Muovo a destra
Turtle.lt(90)                 # Muovo  l'angolo di 90 gradi
Turtle.fd(100)                # Muovo su visto che ho girato la freccia
Turtle.lt(90)
Turtle.fd(100)
Turtle.lt(90)
Turtle.fd(100)


for i in range(4):            #Rifaccio la stessa cosa con un ciclo for
    Turtle.lt(90)
    Turtle.fd(100)


turtle.mainloop()              #In questo modo tengo la finestra aperta


