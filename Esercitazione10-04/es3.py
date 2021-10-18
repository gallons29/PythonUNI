class Riquadro:

    def __init__(self, larghezza, altezza):
        self._larghezza = larghezza
        self._altezza = altezza

    def area(self):
        return (self._larghezza * self._altezza)
    
    def perimeter(self):
        return (self._larghezza * 2 + self._altezza * 2)

def main():
    larghezza_utente = int(input("Inserisci larghezza riquadro: "))
    altezza_utente = int(input("Inserisci altezza riquadro: "))
    riquadro_utente = Riquadro(larghezza_utente, altezza_utente)
    print(f"L'area del tuo riquadro è {riquadro_utente.area()}.\nIl perimetro del tuo riquadro è {riquadro_utente.perimeter()}")
main()