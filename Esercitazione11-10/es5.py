import g2d
CANVAS_W, CANVAS_H = 720, 720
valori_utente = []

def conta_valori_uguali(valori, n):
    contatore = 0
    for val in valori:
        if(val == n):
            contatore += 1
    return contatore

def max_counter(valori):
    val_massimo, val_minimo = massimo_minimo(valori_utente)
    temp_count = 0
    max_count = 0
    for i in range(val_minimo, val_massimo + 1):
        temp_count = conta_valori_uguali(valori, i)
        if(temp_count >= max_count):
            max_count = temp_count
    return max_count


def massimo_minimo(valori):
    massimo = valori[0]
    minimo = valori[0]
    for val in valori:
        if(val >= massimo):
            massimo = val
        if(val <= minimo):
            minimo = val
    return massimo, minimo

def calcola_media_ripetizioni(valori):
    ripetizioni = []
    val_massimo, val_minimo = massimo_minimo(valori_utente)
    for i in range(val_minimo, val_massimo + 1):
        ripetizioni.append(conta_valori_uguali(valori, i))
    somma = 0
    for r in ripetizioni:
        somma += r
    return somma / len(ripetizioni)

def cambia_colore(valore, valori):
    media = calcola_media_ripetizioni(valori)
    if(valore > media):
        g2d.set_color((20, 125, 245))
    if(valore == media):
        g2d.set_color((161, 255, 10))
    if(valore < media):
        g2d.set_color((255, 0, 0))

def tick():
    val_massimo, val_minimo = massimo_minimo(valori_utente)
    n_valori = (val_massimo - val_minimo) + 1
    
    unit_w = CANVAS_W / n_valori
    unit_h = (CANVAS_H - unit_w) / max_counter(valori_utente)
    
    counter = 0
    altezza = 0
    val_h = CANVAS_H - unit_w
    val_w = 0
    for i in range(val_minimo, val_massimo + 1):
        counter = conta_valori_uguali(valori_utente, i)
        cambia_colore(counter, valori_utente)
        altezza = unit_h * counter
        g2d.draw_text(str(i), (val_w, val_h), unit_w)
        g2d.fill_rect((val_w, val_h - altezza), (unit_w, altezza))
        val_w += unit_w



def main():
    val = int(input("Inserisci un numero, 0 per terminare "))
    while(val != 0):
        valori_utente.append(val)
        val = int(input("Inserisci un numero, 0 per terminare "))

    print(f"Media: {calcola_media_ripetizioni(valori_utente)}")
    g2d.init_canvas((CANVAS_W, CANVAS_H))
    g2d.main_loop(tick)
main()