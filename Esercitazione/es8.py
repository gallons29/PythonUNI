from random import randint

quadrato = 500

n = int(input("Inserisci n: "))
r = 0
x = quadrato / 2
y = quadrato / 2

for i in range(0, n):
    r = randint(0, 3)
    if r == 0:
        y -= 10
    elif r == 1:
        x += 10
    elif r == 2:
        y += 10
    elif r == 3:
        x -= 10
print(f"Coordinate finali: X {x} , Y {y}")
distanza = abs(x) + abs(y)
print(f"Distanza = {distanza}")