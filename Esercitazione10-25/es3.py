def squared_range(val_iniziale, val_finale):
    quadrati = []
    for i in range(val_iniziale, val_finale):
        quadrati.append(i**2)
    
    return quadrati

def main():
    utente_iniziale = int(input("Inserisci il valore iniziale: "))
    utente_finale = int(input("Inserisci il valore finale: "))

    quadrati_utente = squared_range(utente_iniziale, utente_finale)
    print(f"La lista dei quadrati è {quadrati_utente}")
main()