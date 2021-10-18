def count_char(text, char_to_find):
    counter = 0
    for char in text:
        if(char == char_to_find):
            counter += 1
    return counter

def main():
    user_text = input("Inserisci un testo: ")
    user_char = input("Inserisci il carattere da trovare altrimenti scrivi \"exit\" per uscire: ")
    while(user_char != "exit"):
        if(len(user_char) > 1):
            print("Devi inserire un singolo carattere per volta")
        else:
            print(f"Il carattere \"{user_char}\" compare {count_char(user_text, user_char)} volte nel testo \"{user_text}\"")
        user_char = input("Inserisci il carattere da trovare altrimenti scrivi \"exit\" per uscire: ")
main()