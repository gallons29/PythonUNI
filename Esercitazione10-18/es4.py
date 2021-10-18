dati = []

def find_indice(data):
    indice_trovato = 0
    for dato in dati:
        if data >= dato[0]:
            indice_trovato = dati.index(dato) + 1
    return indice_trovato

mm = int(input("Inserisci i millimetri di piogga: "))
while(mm >= 0):
    data = input("Inserisci la data: ")
    indice = find_indice(data)
    dati.insert(indice, (data, mm))

    mm = int(input("Inserisci i millimetri di piogga: "))

print(dati)