import g2d
from random import randint

CANVAS_X = 500
CANVAS_Y = 500

g2d.init_canvas((CANVAS_X, CANVAS_Y))

numero_cerchi = int(g2d.prompt("Inserisci il numero di cerchi "))

raggio = 20

for i in range(numero_cerchi):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    g2d.set_color((r, g, b))

    pos_x = randint(0, CANVAS_X)
    pos_y = randint(0, CANVAS_Y)
    while(pos_x > (CANVAS_X - raggio) or pos_x < raggio):
        pos_x = randint(0, CANVAS_X)
    while(pos_y > (CANVAS_Y - raggio) or pos_y < raggio):
        pos_y = randint(0, CANVAS_Y)
    
    g2d.fill_circle((pos_x, pos_y), raggio)

g2d.main_loop()