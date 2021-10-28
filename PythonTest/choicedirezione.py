from random import choice

dx, dy = 0, -2

dirs = [(2, 0), (0, 2), (0, -2), (-2, 0)]
dirs.remove((-dx, -dy))

dx, dy = choice(dirs)

print(dx, dy)