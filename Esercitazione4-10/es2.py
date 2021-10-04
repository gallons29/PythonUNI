import g2d

ARENA_W, ARENA_H, BALL_D = 500, 500, 20 #BALL_R è il diametro della palla

class Ball:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._dx = 2
    
    def position(self):
        return self._x, self._y
    
    def move(self):
        if self._x + self._dx <= 0:
            self._x = ARENA_W - BALL_D
        elif self._x + self._dx >= ARENA_W + BALL_D:
            self._x = 0
        self._x += self._dx

b1 = Ball(400, 50)

def tick():
    g2d.clear_canvas()
    g2d.fill_circle((b1.position()), BALL_D/2)
    b1.move()

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)
main()