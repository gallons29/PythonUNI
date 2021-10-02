anno = int(input("Inserisci anno: "))

while(anno != 0):
    if(anno % 400 == 0):
        print("Anno secolare bisestile")
    elif(anno % 4 == 0 and anno % 100 != 0):
        print("Anno bisestile")
    else:
        print("Anno non bisestile")
    anno = int(input("Inserisci anno: "))