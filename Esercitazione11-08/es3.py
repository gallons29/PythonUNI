from random import randint

w = int(input("Inserisci la larghezza della matrice: "))
h = int(input("Inserisci l'altezza della matrice: "))
matrice = []

for i in range(h):
    val_matrice = []
    for j in range(w):
        val_matrice.append(randint(0, 16))
    matrice.append(val_matrice)

print(matrice)

with open("Esercitazione11-08/es3.csv", "w") as mat:
    for linea_matrice in matrice:
        for val in linea_matrice:
            #if *ultimo valore della linea*
            #print(val, end='', file=mat)
            #else
            print(val, end=',', file=mat)
        print(file=mat)


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
#devo fare in modo che ogni riga del file non finisca con la virgola come commentato sopra