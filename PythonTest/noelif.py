a = input("First word? ")
b = input("Second word? ")

if a < b:
    print("The words are ordered")
else:
    if a > b:
        print("The words are inverted")
    else:
        print("The words are equal")