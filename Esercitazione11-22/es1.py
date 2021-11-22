def parola_maggiore(parole):
    maggiore = ""
    for i in range(len(parole)):
        if isinstance(parole[i], list): #se l'elemento della lista è un instance di list e quindi è una lista, rimpiazzo quell'elemento col maggiore dei suoi elementi
            parole[i] = parola_maggiore(parole[i])

    for parola in parole: #parole ora è una lista di stringhe, e quindi le confronto con un for
        if parola >= maggiore:
            maggiore = parola
    return maggiore


parole_utente = ["Ann", ["Bart", ["Carol", "Cindy"], "Bob", "Art"], ["Bea"], "Bill"]
parola_maggiore_utente = parola_maggiore(parole_utente)
print(parola_maggiore_utente)