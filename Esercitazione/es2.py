x1 = float(input("Inserisci x del primo punto "))
y1 = float(input("Inserisci y del primo punto "))
x2 = float(input("Inserisci x del secondo punto "))
y2 = float(input("Inserisci y del secondo punto "))

deltaX = x2 - x1
deltaY = y2 - y1

if(deltaX == 0):
    print("Retta verticale")
else:
    m = deltaY / deltaX
    print(f"La pendenza è {m}")