import g2d
from random import randint

g2d.init_canvas((500, 500))

n = int(g2d.prompt("n? "))
puntoX = 0
puntoY = 0

for i in range(n):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    g2d.set_color((r, g, b))
    g2d.fill_rect((puntoX, puntoY), (50, 50))
    puntoX += 50
    if i % 10 == 0 and i != 0:
        puntoY += 50
        puntoX = 0

g2d.main_loop()