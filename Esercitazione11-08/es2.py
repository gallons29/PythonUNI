perc_maiuscole_riga = []
perc_maiuscole_global = 0
n_char = 0 #numero di tutti i caratteri nel file

with open("Esercitazione11-08/file.csv", "r") as frase:
    for linea in frase:
        if linea != '\n':
            upper_counter = 0
            for char in linea.strip():
                n_char += 1
                if char.isupper():
                    upper_counter += 1
                    perc_maiuscole_global += 1
            
            perc_maiuscole_riga.append(upper_counter/len(linea.strip())*100)

perc_maiuscole_global = perc_maiuscole_global / n_char * 100 #perc_maiuscole_global era il numero totale di maiuscole trovate, lo divido per il numero totale di caratteri e moltipliclo per 100 per trovare la percentuale
print(perc_maiuscole_riga) #array contenente le percentuali
print(f"Percentuale di tutte le maiuscole nel file: {perc_maiuscole_global} %")