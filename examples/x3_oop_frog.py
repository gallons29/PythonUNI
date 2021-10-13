#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from actor import Actor, Arena

class Vehicle(Actor):
    def __init__(self, arena, pos: (int, int), dx: int):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._left, self._right = -100, arena.size()[0] + 100
        self._dx = dx
        self._arena = arena
        arena.add(self)

    def move(self):
        if self._x + self._dx < self._left:
            self._x = self._right
        if self._x + self._dx > self._right:
            self._x = self._left
        self._x += self._dx

    def position(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def symbol(self):
        return 0, 0

    def collide(self, other):
        pass

class Frog(Actor):
    def __init__(self, arena, pos: (int, int)):
        self._x0, self._y0 = pos
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._dx, self._dy = 0, 0
        self._speed, self._steps, self._count = 2, 10, 0
        self._arena = arena
        arena.add(self)

    def move(self):
        if self._count > 0:
            self._count -= 1

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

    def position(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def symbol(self):
        return 0, 0

    def collide(self, other):
        self._x, self._y = self._x0, self._y0

    def control(self, keys):
        if "a" in keys and self._count == 0:
            self._count = self._steps
            self._dx, self._dy = -self._speed, 0
        elif "d" in keys and self._count == 0:
            self._count = self._steps
            self._dx, self._dy = +self._speed, 0
        elif "w" in keys and self._count == 0:
            self._count = self._steps
            self._dx, self._dy = 0, -self._speed
        elif "s" in keys and self._count == 0:
            self._count = self._steps
            self._dx, self._dy = 0, +self._speed

def tick():
    frog.control(g2d.current_keys())
    g2d.clear_canvas()
    arena.move_all()
    for a in arena.actors():
        g2d.fill_rect(a.position(), a.size())

def main():
    global arena, frog
    arena = Arena((480, 360))
    frog = Frog(arena, (230, 340))
    Vehicle(arena, (40, 40), 5)
    Vehicle(arena, (80, 80), -5)
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
