class StazioneMeteo:
    def __init__(self, nome):
        self._nome = nome
        self._dati_piovosita = []

    def aggiungi_dato(self, data, mm):
        def find_indice(data):
            indice_trovato = 0
            for dato in self._dati_piovosita:
                if data >= dato[0]:
                    indice_trovato = self._dati_piovosita.index(dato) + 1
            return indice_trovato
        self._dati_piovosita.insert(find_indice(data), (data, mm))
    
    def pioggia_totale(self, data1, data2):
        indice_data1 = -1
        indice_data2 = -1
        for dato in self._dati_piovosita:
            if(data1 == dato[0]):
                indice_data1 = self._dati_piovosita.index(dato)
            if(data2 == dato[0]):
                indice_data2 = self._dati_piovosita.index(dato)
        if(indice_data1 < 0 or indice_data2 < 0):
            print("Una data che hai inserito non è presente.")
            return 0

        return self._dati_piovosita[indice_data1][1] + self._dati_piovosita[indice_data2][1]


def main():
    stazione = StazioneMeteo("Parma")

    mm = int(input("Inserisci i millimetri di piogga: "))
    while(mm >= 0):
        data = input("Inserisci la data: ")
        stazione.aggiungi_dato(data, mm)
        mm = int(input("Inserisci i millimetri di piogga: "))
    
    print(stazione._dati_piovosita)

    data1 = input("Inserisci la prima data per sommare la piogga, altrimenti scrivi \"exit\" per terminare: ")
    while(data1 != "exit"):
        data2 = input("Inserisci la seconda data per sommare la piogga: ")
        somma_pioggia = stazione.pioggia_totale(data1, data2)
        print(f"La somma della pioggia in queste date è {somma_pioggia}")
        data1 = input("Inserisci la prima data per sommare la piogga, altrimenti scrivi \"exit\" per terminare: ")

main()