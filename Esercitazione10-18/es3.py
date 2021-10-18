def genera_config(str):
    configurazioni = []
    for s1 in str:
        for s2 in str:
            for s3 in str:
                configurazioni.append(s1+s2+s3)
    return configurazioni


insieme_simboli = input("Inserisci l'insieme dei simboli ")
lista_configurazioni = genera_config(insieme_simboli)
print(lista_configurazioni)
