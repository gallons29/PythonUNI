def ciao(a, b, c):
    a += 3
    b += 4
    c += 5
    print(a, b, c)
    return a, b, c

def main():
    x, y, z = 1, 3, 5
    x, y, z = ciao(x, y, z)
    print(x, y, z)

main()