valori_utente = []
val = int(input("Inserisci un numero, 0 per terminare "))

while(val != 0):
    valori_utente.append(val)
    val = int(input("Inserisci un numero, 0 per terminare "))

def maggiori_minori(lista_valori):
    maggiori= 0
    minori = 0
    for valore in lista_valori:
        if(valore > lista_valori[len(lista_valori)-1]):
            maggiori += 1
        if(valore < lista_valori[len(lista_valori)-1]):
            minori += 1
    return (maggiori, minori)

print(maggiori_minori(valori_utente))