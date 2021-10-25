def count_chars(text: str, chars: str):
    counters = [0] * len(chars)
    for char in chars:
        for t in text:
            if char == t:
                counters[chars.index(char)] += 1
    return counters

def main():
    testo_utente = input("Inserisci il testo: ")
    caratteri_utente = input("Inserisci i caratteri: ")
    contatori_utente = count_chars(testo_utente, caratteri_utente)
    print(contatori_utente)
main()