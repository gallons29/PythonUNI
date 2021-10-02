import g2d

ARENA_W, ARENA_H = 500, 500
BALL_W, BALL_H = 20, 20
balls = []

class Ball:
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._dx = 5
        self._dy = 5
    
    def move(self):
        if self._x <= 0 or self._x >= ARENA_W - BALL_W:
            self._dx = -self._dx
        if self._y <= 0 or self._y >= ARENA_H - BALL_H:
            self._dy = -self._dy
        
        self._x += self._dx
        self._y += self._dy

    def position(self):
        return self._x, self._y

def crea_pallina():
    if g2d.key_pressed('LeftButton'):
        pos_x, pos_y = g2d.mouse_position()
        if pos_x < ARENA_W - BALL_W and pos_y < ARENA_H - BALL_H: #bug fix che se clickavo tra ARENA_W/H - BALL_W/H e ARENA_W/H la palla era sempre in una posizione di cambio d 
            balls.append(Ball(pos_x, pos_y))

def muovi_palline():
    for ball in balls:
        g2d.draw_image("ball.png", ball.position())
        ball.move()

def tick():
    g2d.clear_canvas()
    crea_pallina()
    muovi_palline()

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)
main()