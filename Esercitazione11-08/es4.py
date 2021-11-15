rows = 0
with open("Esercitazione11-08/es3.csv", "r") as mat:
    valori = []
    for line in mat:
        num = ''
        for val in line:
            if val != ',' and val != '\n':
                num += val
            elif val == '\n':
                rows += 1 
                valori.append(int(num))
                num = ''
            else:
                valori.append(int(num))
                num = ''

cols = len(valori) // rows

valori_medi = []

for x in range(cols):
    sum = 0
    for y in range(rows):
        sum += int(valori[y * cols + x])
    valori_medi.append(sum/rows)

print(valori_medi)