import g2d
from random import randint

quadrato = 500

g2d.init_canvas((quadrato, quadrato))

n = int(g2d.prompt("Inserisci n: "))
r = 0
x = quadrato / 2
y = quadrato / 2

qt_nero = 0 ##"quantità nero": utilizzo solo una variabile per la "quantità" di rosso, verde, blu perchè il nero e le sue "tonalità" hanno la stessa quantità di r, g, b
g2d.set_color((qt_nero, qt_nero, qt_nero))
g2d.draw_line((x - 5, y), (x + 5, y)) #Dato che la lunghezza della riga è 10px, per centrarla alla x, ovvero il punto in cui mi trovo devo farla partire 5px prima e farla finire 5px dopo
g2d.draw_line((x, y - 5), (x, y + 5))

for i in range(0, n):
    r = randint(0, 3)
    if r == 0:
        y -= 10
    elif r == 1:
        x += 10
    elif r == 2:
        y += 10
    elif r == 3:
        x -= 10
    qt_nero += (255/n) ##aumento la quantità r, g, b, "schiarendo" il colore. Aumento di 255/n così che esca sempre una scala lineare di colore. Se per esempio aumentassi di 20, con n=15 avrei colori con valori maggiori di 255, il che risulterebbe un errore.
    g2d.set_color((qt_nero, qt_nero, qt_nero))
    g2d.draw_line((x - 5, y), (x + 5, y))
    g2d.draw_line((x, y - 5), (x, y + 5))
print(f"Coordinate finali: X {x} , Y {y}")
distanza = abs(x) + abs(y)
print(f"Distanza = {distanza}")

g2d.main_loop()