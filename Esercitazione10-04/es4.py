x = 5
y = 5
distanza = 0

for j in range(y+1):
    for i in range(x+1):
        distanza = i - j
        print(abs(distanza), end="\t")
    print()