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


def tick():
    val_massimo, val_minimo = massimo_minimo(valori_utente)
    n_valori = (val_massimo - val_minimo) + 1
    
    unit_h = CANVAS_H / n_valori
    unit_w = CANVAS_W / max_counter(valori_utente)
    
    counter = 0
    lunghezza = 0
    val_w = unit_h
    val_h = 0
    for i in range(val_minimo, val_massimo + 1):
        counter = conta_valori_uguali(valori_utente, i)
        lunghezza = unit_w * counter
        g2d.draw_text(str(i), (0, val_h), unit_h)
        g2d.fill_rect((val_w, val_h), (lunghezza, unit_h))
        val_h += unit_h



def main():
    val = int(input("Inserisci un numero, 0 per terminare "))
    while(val != 0):
        valori_utente.append(val)
        val = int(input("Inserisci un numero, 0 per terminare "))

    g2d.init_canvas((CANVAS_W, CANVAS_H))
    g2d.main_loop(tick)
main()