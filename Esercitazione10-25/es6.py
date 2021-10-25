class Testo:
    def __init__(self, text):
        self._text = text
    
    def count_chars(self, chars):
        counters = [0] * len(chars)
        for char in chars:
            for t in self._text:
                if char == t:
                    counters[chars.index(char)] += 1
        return counters

def main():
    testo_utente = Testo(input("Inserisci il testo: "))
    caratteri_utente = input("Inserisci i caratteri da contare o .. (due punti) per uscire: ")

    while(caratteri_utente != ".."):
        print(testo_utente.count_chars(caratteri_utente))
        caratteri_utente = input("Inserisci i caratteri da contare o .. (due punti) per uscire: ")
main()