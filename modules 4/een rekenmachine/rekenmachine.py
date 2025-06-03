from calculation import calculations

def main():
    firstRound = True
    result = None  # Initialiseer 'result' buiten de loop
    while True:
        if firstRound:
            firstRound = False
            choice = input("Wat wilt u doen?\nA) Optellen\nB) Aftrekken\nC) Vermenigvuldigen\nD) Delen\nE) Ophogen\nF) Verlagen\nG) Verdubbelen\nH) Halveren\nKeuze: ").lower()
            if choice in ['e', 'f', 'g', 'h']:
                n1 = float(input("Geef het getal in: "))
                n2 = 1 if choice in ['e', 'f'] else 2
            else:
                n1 = float(input("Geef het eerste getal in: "))
                n2 = float(input("Geef het tweede getal in: "))
        else:
            print(f"\nUitkomst: {result}")
            choice = input("Wil je wat met de uitkomst doen? A) Optellen, B) Aftrekken, C) Vermenigvuldigen, D) Delen, E) Ophogen, F) Verlagen, G) Verdubbelen, H) Halveren, I) Niets: ").lower()
            if choice == 'i':
                print("Rekenmachine is gestopt.")
                break
            if choice in ['e', 'f']:
                n2 = 1
            elif choice in ['g', 'h']:
                n2 = 2
            else:
                try:
                    n2 = float(input("Geef het tweede getal in: "))
                except ValueError:
                    print("Ongeldige invoer voor het tweede getal. Probeer het opnieuw.")
                    continue
            n1 = result

        # Mapping user input to dictionary keys
        key_map = {
            'a': 'add',
            'b': 'subtract',
            'c': 'multiply',
            'd': 'divide',
            'e': 'add',
            'f': 'subtract',
            'g': 'multiply',
            'h': 'divide'
        }

        operation = key_map.get(choice)
        if operation in calculations:
            try:
                result = calculations[operation](n1, n2)
                symbol_map = {'add': '+', 'subtract': '-', 'multiply': 'x', 'divide': ':'}
                symbol = symbol_map[operation]
                print(f"{n1} {symbol} {n2} = {result}")
            except Exception as e:
                print(f"Fout bij berekenen: {e}")
        else:
            print("Onbekende keuze.")

if __name__ == "__main__":
    main()
