import g2d
CANVAS_W, CANVAS_H = 720, 720

valori_utente = []
val = int(input("Inserisci un numero, 0 per terminare "))

while(val != 0):
    valori_utente.append(val)
    val = int(input("Inserisci un numero, 0 per terminare "))


def calcolo_valori_uguali(valori, n):
    contatore = 0
    for val in valori:
        if(val == n):
            contatore += 1
    return contatore

g2d.init_canvas((CANVAS_W, CANVAS_H))
lunghezza = calcolo_valori_uguali(valori_utente, valori_utente[0]) * 10
g2d.fill_rect((0, 0), (lunghezza, 20))

g2d.main_loop()