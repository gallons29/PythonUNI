n = int(input("n (massimo 3): "))
while(n > 3):
    print("n non deve essere maggiore di 3")
    n = int(input("n non deve essere maggiore di 3\n reiserisci n: "))

combinazioni = ""
for i in range(1, n**2+1):
    combinazioni = combinazioni [i:] + str(i) + combinazioni[:n**2+1]
#se n = 2 combinazioni sarà "4321", se n = 3 sarà "987654321". Nel caso fosse 4 (in questo caso non potrà esserlo), questo metodo non andrebbe più bene.

def anagram(comb: str) -> [str]:
    if len(comb) == 0:
        return ['']

    result = []
    for i in range(len(comb)):
        c = comb[i]
        rest = comb[:i] + comb[i + 1:]
        for p in anagram(rest):
            result.append(c + p)
    return result

print(anagram(combinazioni))

cols = n
rows = n #il numero di righe e colonne coincide con n

def somme_quadrato_magico(mat: list) -> list:
    raise NotImplementedError('Da fare')

combinazioni_magiche = []
for combinazione in combinazioni:
    matrice = combinazione.split('')
    somme = somme_quadrato_magico(matrice)
    val = somme[0] #prendo come riferimento il primo valore
    for v in somme:
        if v != val and not v in somme: #controllo per tutti i valori delle somme diverse dal primo valore. se nessun altro valore è presente in somme allora significa che tutti i valori di somme sono uguali al primo e quindi sono tutte uguali: quadrato magico
            combinazioni_magiche.append(matrice)