def somma_valori(valori: list) -> int:
    somma = 0
    for val in valori:
        somma += val
    return somma

lanci = []
somma_lanci = [] #lista con elementi i conteggi di ogni riga
with open("Esercitazione11-22/es2.csv", "r") as d:
    for line in d:
        if line != '\n':
            lancio = line.strip().split(',')
            lanci.append(lancio)

    for lancio in lanci: #lanci è una lista di liste. le liste che ha come elementi contengono la terna di valori dei dadi
        for i, v in enumerate(lancio):
            lancio[i] = int(v)
        somma_lanci.append(somma_valori(lancio))

    # print(somma_lanci)

counter = [0] * 18

for val in somma_lanci:
    indice = val - 1
    counter[indice] += 1

print(counter)