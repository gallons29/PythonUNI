import g2d

ARENA_W, ARENA_H, BALL_D = 500, 500, 20 #BALL_R è il diametro della palla

class Ball:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._dx = 2
        self._dy = 0
    
    def position(self):
        return self._x, self._y
    
    def move(self):
        if g2d.key_pressed('w'):
            self._dy = -2
            self._dx = 0
        elif g2d.key_pressed('s'):
            self._dy = 2
            self._dx = 0
        elif g2d.key_pressed('a'):
            self._dx = -2
            self._dy = 0
        elif g2d.key_pressed('d'):
            self._dx = 2
            self._dy = 0

        self._x = (self._x + self._dx) % (ARENA_W + BALL_D)
        self._y = (self._y + self._dy) % (ARENA_H + BALL_D)

b1 = Ball(400, 50)

def tick():
    g2d.clear_canvas()
    g2d.fill_circle((b1.position()), BALL_D/2)
    b1.move()

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)
main()