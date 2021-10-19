#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from random import choice, randrange
from time import time
from actor import Actor, Arena

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
        self._w, self._h = 20, 20
        self._arena = arena
        arena.add(self)
        self._visible = True

    def move(self):
        dx = choice([-5, 0, 5])
        dy = choice([-5, 0, 5])
        arena_w, arena_h = self._arena.size()
        self._x = (self._x + dx) % arena_w
        self._y = (self._y + dy) % arena_h

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
            return 20, 0
        return 20, 20


class PacMan(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._speed = 2
        self._dx, self._dy = 0, 0
        self._lives = 3
        self._last_collision = 0
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > arena_h - self._h:
            self._y = arena_h - self._h

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - self._w:
            self._x = arena_w - self._w

    def control(self, keys):
        if self._x % 8 == 0 and self._y % 8 == 0:
                
            u, d, l, r = "ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"
            #u, d, l, r = "w", "s", "a", "d"

            if u in keys: self._dx, self._dy = 0, -self._speed
            elif d in keys: self._dx, self._dy = 0, self._speed
            
            if l in keys: self._dx, self._dy = -self._speed, 0
            elif r in keys: self._dx, self._dy = self._speed, 0

    def lives(self) -> int:
        return self._lives

    def collide(self, other):
        if self._arena.count() - self._last_collision < 30:
            return
        self._last_collision = self._arena.count()
        if isinstance(other, Ghost):
            self._lives = 0
        elif isinstance(other, Ball):
            self._lives -= 1

    def position(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def symbol(self):
        return 0, 20


def print_arena(arena):
    for a in arena.actors():
        print(type(a).__name__, '@', a.position())


def main():
    arena = Arena((480, 360))
    Ball(arena, (40, 80))
    Ball(arena, (80, 40))
    Ghost(arena, (120, 80))

    for i in range(25):
        print_arena(arena)
        arena.move_all()

main()  # call main to start the program

