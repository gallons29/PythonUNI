data = [4, 5, 6, 1, 7, 8, 9, 2, 8, 7, 6, 5]

rows = 3
cols = len(data) // rows # 4

for i, v in enumerate(data):
    print(v, end="\n" if i % cols == cols - 1 else ",")