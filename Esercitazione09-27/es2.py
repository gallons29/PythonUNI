x1 = float(input("Inserisci x del primo punto "))
y1 = float(input("Inserisci y del primo punto "))
x2 = float(input("Inserisci x del secondo punto "))
y2 = float(input("Inserisci y del secondo punto "))

dx = x2 - x1
dy = y2 - y1

if(dx == 0):
    print("Retta verticale")
else:
    m = dy / dx
    print(f"La pendenza è {m}")