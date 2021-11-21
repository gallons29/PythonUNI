#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from random import choice, randrange, randint
from time import time
from actor import Actor, Arena
import g2d
from pacman_map import in_wall, board
import math

DEFAULT_BOARD = board[:]

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
    def __init__(self, arena, pos, color):
        self._x, self._y = pos
        self._w, self._h = 16, 16
        self._arena = arena
        arena.add(self)
        self._visible = True
        # self._check_direzione = 0
        self._dx, self._dy = choice([(2, 0), (0, 2), (0, -2), (-2, 0)])
        self._color = color
        if self._color == 'red':
            self._symbols = [(0, 64), (32, 64), (64, 64), (96, 64)]
        elif self._color == 'pink':
            self._symbols = [(0, 80), (32, 80), (64, 80), (96, 80)]
        elif self._color == 'cyan':
            self._symbols = [(0, 96), (32, 96), (64, 96), (96, 96)]
        elif self._color == 'orange':
            self._symbols = [(0, 112), (32, 112), (64, 112), (96, 112)]

    def move(self):
        
        def cambia_direzione(dx, dy):
            dirs = [(2, 0), (0, 2), (0, -2), (-2, 0)]
            dirs.remove((-dx, -dy))
            dx, dy = choice(dirs)
            while in_wall(self._x + dx, self._y + dy):
                dx, dy = choice(dirs)
            return dx, dy


        arena_w, arena_h = self._arena.size()
        if not in_wall(self._x + self._dx, self._y + self._dy):
            self._x = (self._x + self._dx) % arena_w
            self._y = (self._y + self._dy) % arena_h
        if self._x % 8 == 0 and self._y % 8 == 0:
            self._dx, self._dy = cambia_direzione(self._dx, self._dy)

        

    def collide(self, other):
        pass

    def position(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def symbol(self):
        coordinate_finali = self._symbols[1]
        if self._dx > 0 and self._dy == 0:
            coordinate_finali = self._symbols[0]
        if self._dx < 0 and self._dy == 0:
            coordinate_finali = self._symbols[1]
        if self._dx == 0 and self._dy < 0:
            coordinate_finali = self._symbols[2]
        if self._dx == 0 and self._dy > 0:
            coordinate_finali = self._symbols[3]
        
        return coordinate_finali
    def a_type(self):
        return 'ghost'


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
        self._anim = 0
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        self.control(g2d.current_keys())
        if not in_wall(self._x + self._dx, self._y + self._dy):
            self._y = (self._y + self._dy) % (arena_h)
            self._x = (self._x + self._dx) % (arena_w)

#impedire di cambiare symbol verso quella del muro quando si scontra
    def control(self, keys):
        if self._x % 8 == 0 and self._y % 8 == 0:
                
            # u, d, l, r = "ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"
            u, d, l, r = "w", "s", "a", "d"

            if u in keys and not in_wall(self._x, self._y - self._speed): self._dx, self._dy = 0, -self._speed
            elif d in keys and not in_wall(self._x, self._y + self._speed): self._dx, self._dy = 0, self._speed

            if l in keys and not in_wall(self._x - self._speed, self._y): self._dx, self._dy = -self._speed, 0
            elif r in keys and not in_wall(self._x + self._speed, self._y): self._dx, self._dy = self._speed, 0

    def lives(self) -> int:
        return self._lives

    def collide(self, other):
        self._arena.remove(self)
        is_game_over(True)
        # print(self.position(), other.position())

    def position(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def symbol(self):
        coordinate_simboli = [[(0, 0), (16, 0), (32, 0)], [(0, 16), (16, 16), (32, 0)], [(0, 32), (16, 32), (32, 0)], [(0, 48), (16, 48), (32, 0)]]
        # coordinate per quando si muove verso destra sono all'indice 0, sinistra indice 1 e così via.
        coordinate_finali = (32, 0)
        if self._dx > 0 and self._dy == 0:
            coordinate_finali = coordinate_simboli[0][self._count_anim]
        if self._dx < 0 and self._dy == 0:
            coordinate_finali = coordinate_simboli[1][self._count_anim]
        if self._dx == 0 and self._dy < 0:
            coordinate_finali = coordinate_simboli[2][self._count_anim]
        if self._dx == 0 and self._dy > 0:
            coordinate_finali = coordinate_simboli[3][self._count_anim]
        
        if self._anim >= 3 and not in_wall(self._x + self._dx, self._y + self._dy):
            self._count_anim += self._delta_animazione
            if self._count_anim == 2:
                self._delta_animazione = -1
            if self._count_anim == 0:
                self._delta_animazione = 1
            self._anim = 0
        self._anim += 1

        return coordinate_finali
    def a_type(self):
        return 'pacman'


def print_arena(arena):
    for a in arena.actors():
        print(type(a).__name__, '@', a.position())



arena = Arena((232, 256))
pacman = PacMan(arena, (112, 184))
arena.add(Ghost(arena, (72,88), 'red'))
arena.add(Ghost(arena, (88,88), 'pink'))
arena.add(Ghost(arena, (112,88), 'cyan'))
arena.add(Ghost(arena, (96,88), 'orange'))

#per controllare quando non ci sono più biscotti (quindi quando il giocatore vince) uso una lista di len(board) elementi (n di righe), se nella riga è presente almeno un biscotto, l'elemento all'indice di quella riga varrà 1.
#nella funzione tick setterò a 0 gli indici in cui non è presente nessun biscotto
biscuits_presences = [1] * len(board) #inizializzo con tutti 1 perchè la board inizialmente è piena di biscotti
#anche se ci sono righe in cui non è presente nessun biscotto inizialmente (es. la prima è solo #), l'elemento all'indice di queste righe verrà settato a 0 al primo controllo
#avrei potuto (per essere più preciso) inizializzare la lista con len(board) elementi vuoti e a ogni controllo (nella funzione tick) assegnare 1 o 0 agli elementi ogni volta

def biscuits(pos, b):
    x, y = pos
    c, r, w, h = math.ceil(x/8), math.ceil(y/8), 2, 2
    for i in range(r, r+h):
        for j in range(c, c+w):
            if b[i][j] == '-':
                b[i] = b[i][:c+1] + ' ' + b[i][c+w:]
            if b[i][j] == '+':
                b[i] = b[i][:c+1] + ' ' + b[i][c+w:]
    return b

def draw_biscuits(b):
    for line in range(0, len(b)):
        for item in range(0, len(b[line])):
            if b[line][item] == '-':
                item_pos = item * 8-8, line * 8-8
                g2d.draw_image_clip("https://tomamic.github.io/images/sprites/pac-man.png", (160, 48), (16, 16), item_pos)
            if b[line][item] == '+':
                item_pos = item * 8-8, line * 8-8
                g2d.draw_image_clip("https://tomamic.github.io/images/sprites/pac-man.png", (176, 48), (16, 16), item_pos)

class Board:
    def __init__(self):
        self._b = DEFAULT_BOARD[:]
    
    def reset(self):
        self._b = DEFAULT_BOARD[:]
        return self._b
    
    def board(self):
        return self._b

    def update_b(self, b):
        self._b = b[:]
game_board = Board()

def is_game_over(lost):
    #se non è presente 1 in biscuit_presences vuol dire che in tutte le righe della board non ci sono biscotti, per cui il giocatore ha vinto
    if not lost:
        if not 1 in biscuits_presences:
            g2d.alert("You won!")
            return True
        else:
            return False
    else:
        g2d.alert("You lost!")
        return True

def tick():
    if is_game_over(False):
        print('dentro')
        for a in arena.actors():
            arena.remove(a)
        arena.add(PacMan(arena, (112, 184)))
        arena.add(Ghost(arena, (8,8)))
        b = game_board.reset()
        for a in arena.actors():
            if a.a_type() == 'pacman':
                pacman = a


    arena.move_all()
    g2d.clear_canvas()
    g2d.draw_image("https://tomamic.github.io/images/sprites/pac-man-bg.png", (0, 0))
    

    for a in arena.actors():
        if a.symbol() != None:
            g2d.draw_image_clip("https://tomamic.github.io/images/sprites/pac-man.png", a.symbol(), a.size(), a.position())
        else:
            g2d.fill_rect(a.position(), a.size())
        if a.a_type() == 'pacman':
            pacman = a

    b = biscuits(pacman.position(), game_board.board())
    draw_biscuits(b)

    for i in range(len(b)):
        if not '-' in b[i] and not '+' in b[i]:
            biscuits_presences[i] = 0
        else:
            biscuits_presences[i] = 1

        



def main():
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()