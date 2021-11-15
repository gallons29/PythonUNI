from random import randint

cols = int(input("Inserisci la larghezza della matrice: "))
rows = int(input("Inserisci l'altezza della matrice: "))
matrice = []

for i in range(cols * rows):
    matrice.append(randint(0, 16))

print(matrice)

with open("Esercitazione11-08/es3.csv", "w") as mat:
    for i, v in enumerate(matrice):
        print(v, end="\n" if i % cols == cols - 1 else ",", file=mat)


valore_utente = int(input("Inserisci un valore da cercare e contare nella matrice: "))
counter_valore_utente = 0

with open("Esercitazione11-08/es3.csv", "r") as mat:
    valori = []
    for line in mat:
        valori = line.strip().split(',')
        for valore in valori:
            if valore_utente == int(valore):
                counter_valore_utente += 1

print(f"Il valore {valore_utente} è presente {counter_valore_utente} volte.")