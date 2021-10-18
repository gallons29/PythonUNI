class Espressioni_Quadratiche:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    
    def calcolo_espressione(self, x):
        return self._a * (x ** 2) + self._b * x + self._c

def main():
    a = int(input("Inserisci a: "))
    b = int(input("Inserisci b: "))
    c = int(input("Inserisci c: "))
    espressione = Espressioni_Quadratiche(a, b, c)
    quante_x = int(input("Quante x vuoi inserire? "))
    for i in range(quante_x):
        x = int(input("Inserisci x: "))
        print(f"Il risultato è: {espressione.calcolo_espressione(x)}")

main()