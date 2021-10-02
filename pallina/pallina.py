import g2d
from random import randint

ARENA_W, ARENA_H, BALL_W, BALL_H = 500, 500, 20, 20

class Ball:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._dx = 5
        self._dy = 5
    
    def position(self):
        return self._x, self._y
    
    def move(self):
        if not 0 <= self._x + self._dx <= ARENA_W - BALL_W:
            self._dx = -self._dx
        if not 0 <= self._y + self._dy <= ARENA_H - BALL_H:
            self._dy = -self._dy
        self._x += self._dx
        self._y +=self._dy

b1 = Ball(150, 20)
b2 = Ball(300, 50)

def tick():
    g2d.clear_canvas()
 
    g2d.draw_image("ball.png", b1.position())

    g2d.draw_image("ball.png", b2.position())
    
    b1.move()
    b2.move()


def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()