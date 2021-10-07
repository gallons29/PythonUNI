import g2d

ARENA_W, ARENA_H, BALL_D = 500, 500, 20 #BALL_R è il diametro della palla

class HeroBall:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._dx = 0
        self._dy = 0
    
    def position(self):
        return self._x, self._y

    def go_up(self):
        self._dy = -5
        self._dx = 0

    def go_down(self):
        self._dy = 5
        self._dx = 0

    def go_left(self):
        self._dx = -5
        self._dy = 0

    def go_right(self):
        self._dx = 5
        self._dy = 0

    def move(self):
        if g2d.key_pressed('w'):
            self.go_up()
        elif g2d.key_pressed('s'):
            self.go_down()
        elif g2d.key_pressed('a'):
            self.go_left()
        elif g2d.key_pressed('d'):
            self.go_right()

        self._x += self._dx
        self._y += self._dy

b1 = HeroBall(400, 50)

def tick():
    g2d.clear_canvas()
    g2d.fill_circle((b1.position()), BALL_D/2)
    b1.move()

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)
main()