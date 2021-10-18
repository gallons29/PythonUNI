class Text():
    def __init__(self, text):
        self._text = text
    
    def count_char(self, char_to_find):
        counter = 0
        for char in self._text:
            if(char == char_to_find):
                counter += 1
        return counter

def main():
    user_text1 = Text(input("Inserisci un testo: "))
    user_char = input("Inserisci il carattere da trovare altrimenti scrivi \"exit\" per uscire: ")
    while(user_char != "exit"):
        if(len(user_char) > 1):
            print("Devi inserire un singolo carattere per volta")
        else:
            print(f"Il carattere \"{user_char}\" compare {user_text1.count_char(user_char)} volte nel testo \"{user_text1._text}\"")
        user_char = input("Inserisci il carattere da trovare altrimenti scrivi \"exit\" per uscire: ")
main()