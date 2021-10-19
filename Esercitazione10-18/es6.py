def maiuscolo_asterischi(str):
    maiuscolo = False
    new_str = ""
    for char in str:
        if(char == '*'):
            maiuscolo = not maiuscolo
        elif not maiuscolo:
            new_str += char
        else:
            new_str += char.upper()
    return new_str
    
def main():
    user_text = input("Inserisci un testo: ")
    text_maiuscolo = maiuscolo_asterischi(user_text)
    print(text_maiuscolo)
main()