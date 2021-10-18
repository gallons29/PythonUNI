class Espressioni_Polinomiali:
    def __init__(self, n):
        self._n = n
    
    def inserimento_coefficienti(self):
        self._coefficienti = []
        for i in range(self._n + 1):
            self._coefficienti.append(int(input(f"Inserisci il coefficiente per n = {i}: ")))
    
    def calcolo_espressione(self, x):
        risultato = 0
        for i in range(self._n + 1):
            risultato += self._coefficienti[i] * (x ** i)
        return risultato

def main():
    n = int(input("Inserisci n: "))
    espressione = Espressioni_Polinomiali(n)
    espressione.inserimento_coefficienti()
    x = int(input("Inserisci x: "))
    print(f"Risultato: {espressione.calcolo_espressione(x)}")
main()