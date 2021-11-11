def potenza(x, n):
    if n == 0:
        return 1
    return x * potenza(x, n - 1)

def main():
    x_utente = int(input("Inserisci x: "))
    n_utente = int(input("Inserisci l'esponente: "))
    print(f"{x_utente} elevato alla {n_utente} = {potenza(x_utente, n_utente)}")
main()