import g2d
from random import randint

ARENA_W, ARENA_H, BALL_D = 500, 500, 20
check_direzione = 0

class WanderingBall:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._dx = 2
        self._dy = 0
        self._direzione = 3 #parte da direzione destra
    
    def position(self):
        return self._x, self._y

    def cambia_direzione(self):
        global check_direzione
        self._direzione = randint(1,4) #1: alto, 2: basso, 3: destra, 4: sinistra
        if self._direzione == 1 and check_direzione != 2: #check_direzione ora è la direzione precedente, l'opposto della direzione 1 che è alto è 2, basso.
            check_direzione = self._direzione
            return (0, -2) #alto: dx = 0, dy = negativo
        if(self._direzione == 2 and check_direzione != 1):
            check_direzione = self._direzione
            return (0, 2) #basso: dx = 0, dy = positivo
        if(self._direzione == 3 and check_direzione != 4):
            check_direzione = self._direzione
            return (2, 0) #destra: dx = positivo, dy = 0
        if(self._direzione == 4 and check_direzione != 3):
            check_direzione = self._direzione
            return (-2, 0) #sinistra: dx = negativo, dy = 0
        return (self._dx, self._dy) #ritorna nel caso la direzione casuale sia uguale a quella precedente
    
    def move(self):
        self._x += self._dx
        self._y += self._dy
        if self._x % 8 == 0 and self._y % 8 == 0:
            self._dx, self._dy = self.cambia_direzione()

b1 = WanderingBall(250, 240) #la y deve essere inizialmente multiplo di 8 altrimenti la condizione entrambi multipli di 8 non si avvererà mai

def tick():
    g2d.clear_canvas()
    g2d.fill_circle((b1.position()), BALL_D/2)
    b1.move()

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)
main()