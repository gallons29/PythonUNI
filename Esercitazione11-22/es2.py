from random import randint

def lancia_terna_dadi() -> list:
    results = [] * 3
    for i in range(3):
        results.append(randint(1,6))
    return results

n = int(input("Numero di lanci: "))

with open("Esercitazione11-22/es2.csv", "w") as d:
    for i in range(n):
        dadi = lancia_terna_dadi()
        for i, v in enumerate(dadi):
            print(v, end='\n' if i == 2 else ',', file=d)

    
