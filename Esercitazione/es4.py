risposta_sbagliata = False
nome = input("What is your name? ")
if(nome == "Lancelot"):
    quest = input("What is your quest? ")
    if(quest == "Holy Grail"):
        color = input("What is your favorite color? ")
        if(color == "Blue"):
            print("Right. Off you go.")
        else:
            risposta_sbagliata = True
    else:
        risposta_sbagliata = True
else:
    risposta_sbagliata = True

if(risposta_sbagliata):
    print("Down into the Gorge of Ethernal Peril!")