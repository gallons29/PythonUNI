from random import choice

n = int(input("n? "))
x, y, dx, dy = 0, 0, 0, 0

for _ in range(n):
    
    directions = [(0, -10), (10, 0), (0, 10), (-10, 0)]
    opposite = (-dx, -dy)
    if opposite in directions:
        directions.remove(opposite) # No turning back

    dx, dy = choice(directions)
    #assert((dx, dy) != opposite)  #  check, always true
    x += dx
    y += dy
    print(x, y, dx, dy, sep="\t")