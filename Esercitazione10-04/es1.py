def cels_to_fahr(cels: float):
    return (1.8 * cels + 32)

def main():
    t_utente = float(input("Temperatura in gradi Celsius: "))
    fahr = cels_to_fahr(t_utente)
    print(f"Temperatura convertita in gradi Fahrenheit: {fahr}")
main()