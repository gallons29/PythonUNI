import math

def mcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return mcd(b, r)


def main():
    print(mcd(15, 50))
main()