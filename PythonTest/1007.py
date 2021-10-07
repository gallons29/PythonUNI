import g2d
import random
ARENA_W, ARENA_H = 500, 500

class Animal:
    def say(self):
        raise NotImplementedError("Abstract method")

class Dog(Animal):
    def __init__(self, name):
        self._name = name

    def say(self):
        print(f"I am {self._name} Dog. I say: WOOF")

class Cat(Animal):
    def __init__(self, name):
        self._name = name

    def say(self):
        print(f"I am {self._name} Dog. I say: MEOW")

d = Dog("Danny")
c = Cat("Candy")

animals = [d, c]

for animal in animals:
    animal.say()

class Actor:
    def move(self):
        raise NotImplementedError("Abstract method")

class Ghost(Actor):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def move(self):
        dx = random.choice([-5, 0, 5])
        dy = random.choice([-5, 0, 5])
        self._x = (self._x + dx) % ARENA_W
        self._y = (self._y + dy) % ARENA_H
    
    def position(self):
        return self._x, self._y
        
g = Ghost(100, 120)

def tick():
    g2d.clear_canvas()
    g.move()
    g2d.fill_circle((g.position()), 5)

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)
main()