import math

class Sphere:
    def __init__(self, r: float):
        self._r = r

    def area(self):
        return 4 * math.pi * (self._r ** 2)

    def volume(self):
        return 4/3 * math.pi * (self._r ** 3)


raggio_utente = float(input("Inserisci la lunghezza del raggio (cm): "))
sfera_utente = Sphere(raggio_utente)
print(f"L'area della sfera è {sfera_utente.area()} cm²\nIl volume della sfera è {sfera_utente.volume()} cm³")