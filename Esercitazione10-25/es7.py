#NON FINITO
#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from random import choice, randrange, randint
from time import time
from actor import Actor, Arena
import g2d
from pacman_map import in_wall

class Ball(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._speed = 5
        self._dx, self._dy = self._speed, self._speed
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        if not (0 <= self._x + self._dx <= arena_w - self._w):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= arena_h - self._h):
            self._dy = -self._dy
        self._x += self._dx
        self._y += self._dy

    def collide(self, other):
        if not isinstance(other, Ghost):
            x, y = other.position()
            if x < self._x:
                self._dx = self._speed
            else:
                self._dx = -self._speed
            if y < self._y:
                self._dy = self._speed
            else:
                self._dy = -self._speed

    def position(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def symbol(self):
        return 0, 0


class Ghost(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = 16, 16
        self._arena = arena
        arena.add(self)
        self._visible = True
        self._check_direzione = 0
        self._dx, self._dy = 0, 0

    def move(self):
        
        def cambia_direzione():
            self._direzione = randint(1,4) #1: alto, 2: basso, 3: destra, 4: sinistra
            if self._direzione == 1 and self._check_direzione != 2: #self._check_direzione ora è la direzione precedente, l'opposto della direzione 1 che è alto è 2, basso.
                self._check_direzione = self._direzione
                return (0, -2) #alto: dx = 0, dy = negativo
            if(self._direzione == 2 and self._check_direzione != 1):
                self._check_direzione = self._direzione
                return (0, 2) #basso: dx = 0, dy = positivo
            if(self._direzione == 3 and self._check_direzione != 4):
                self._check_direzione = self._direzione
                return (2, 0) #destra: dx = positivo, dy = 0
            if(self._direzione == 4 and self._check_direzione != 3):
                self._check_direzione = self._direzione
                return (-2, 0) #sinistra: dx = negativo, dy = 0
            return (self._dx, self._dy) #ritorna nel caso la direzione casuale sia uguale a quella precedente

        arena_w, arena_h = self._arena.size()
        self._x = (self._x + self._dx) % arena_w
        self._y = (self._y + self._dy) % arena_h
        if self._x % 8 == 0 and self._y % 8 == 0:
            self._dx, self._dy = cambia_direzione()

        if randrange(100) == 0:
            self._visible = not self._visible

    def collide(self, other):
        pass

    def position(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def symbol(self):
        if self._visible:
            return 0, 64
        return 128, 80


class PacMan(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = 16, 16
        self._speed = 2
        self._dx, self._dy = 0, 0
        self._lives = 3
        self._last_collision = 0
        self._arena = arena

        self._delta_animazione = 1
        self._count_anim = 0
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        if not (in_wall(self._x, self._y + self._dy)):
            self.control(g2d.current_keys())
            self._y += self._dy
            if self._y < 0:
                self._y = 0
            elif self._y > arena_h - self._h:
                self._y = arena_h - self._h
        if not (in_wall(self._x + self._dx, self._y)):
            self.control(g2d.current_keys())
            self._x += self._dx
            if self._x < 0:
                self._x = 0
            elif self._x > arena_w - self._w:
                self._x = arena_w - self._w
        print(f"x {self._x} y {self._y}")
#impedire di cambiare symbol verso quella del muro quando si scontra
    def control(self, keys):
        if self._x % 8 == 0 and self._y % 8 == 0:
                
            # u, d, l, r = "ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"
            u, d, l, r = "w", "s", "a", "d"

            if u in keys: self._dx, self._dy = 0, -self._speed
            elif d in keys: self._dx, self._dy = 0, self._speed
            
            if l in keys: self._dx, self._dy = -self._speed, 0
            elif r in keys: self._dx, self._dy = self._speed, 0

    def lives(self) -> int:
        return self._lives

    def collide(self, other):
        self._arena.remove(self)
        # print(self.position(), other.position())

    def position(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def symbol(self):
        coordinate_simboli = [[(0, 0), (16, 0), (32, 0)], [(0, 16), (16, 16), (32, 0)], [(0, 32), (16, 32), (32, 0)], [(0, 48), (16, 48), (32, 0)]]
        # coordinate per quando si muove verso destra sono all'indice 0, sinistra indice 1 e così via.
        coordinate_finali = (0, 0)
        if self._dx > 0 and self._dy == 0:
            coordinate_finali = coordinate_simboli[0][self._count_anim]
        if self._dx < 0 and self._dy == 0:
            coordinate_finali = coordinate_simboli[1][self._count_anim]
        if self._dx == 0 and self._dy < 0:
            coordinate_finali = coordinate_simboli[2][self._count_anim]
        if self._dx == 0 and self._dy > 0:
            coordinate_finali = coordinate_simboli[3][self._count_anim]
        
        self._count_anim += self._delta_animazione
        if self._count_anim == 2:
            self._delta_animazione = -1
        if self._count_anim == 0:
            self._delta_animazione = 1
        return coordinate_finali


def print_arena(arena):
    for a in arena.actors():
        print(type(a).__name__, '@', a.position())



arena = Arena((232, 256))
pacman = PacMan(arena, (40, 40))
#fantasma = Ghost(arena, (80,80))

def tick():
    arena.move_all()
    g2d.clear_canvas()
    g2d.draw_image("https://tomamic.github.io/images/sprites/pac-man-bg.png", (0, 0))


    for a in arena.actors():
        if a.symbol() != None:
            g2d.draw_image_clip("https://tomamic.github.io/images/sprites/pac-man.png", a.symbol(), a.size(), a.position())
        else:
            g2d.fill_rect(a.position(), a.size())

def main():
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()