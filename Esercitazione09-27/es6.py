numero = int(input("Inserisci numero "))
massimo = numero
minimo = numero

while(numero >= 0):
    numero = int(input("Inserisci numero "))
    if(numero >= 0):
        if(numero >= massimo):
            massimo = numero
        if(numero <= minimo):
            minimo = numero
    else:
        print(f"Massimo: {massimo}. Minimo: {minimo}")    