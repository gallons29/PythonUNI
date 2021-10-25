import math

def sphere_volume(r: float):
    return 4/3 * math.pi * (r ** 3)

def main():
    raggio_utente = float(input("Inserisci la lunghezza del raggio (cm): "))
    volume_sfera_utente = sphere_volume(raggio_utente)
    print(f"Il volume della sfera di raggio {raggio_utente} cm è {volume_sfera_utente} cm³")
main()