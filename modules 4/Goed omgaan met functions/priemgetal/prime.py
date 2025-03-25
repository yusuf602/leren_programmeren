from functions import is_prime, priem_tot_en_met, first_n_primes, primes_between

def main():
    print("\n PRIEMGETALLEN GENERATOR ")
    print("1️ Priemgetallen tot en met een bepaald getal")
    print("2️ De eerste N priemgetallen")
    print("3️ Priemgetallen tussen twee getallen")
    print("4️ Stoppen\n")

    while True:
        keuze = input("Welke functie wil je gebruiken? (1/2/3/4): ").strip()

        if keuze == "1":
            try:
                n = int(input("Tot welk getal wil je priemgetallen? "))
                resultaat = priem_tot_en_met(n)
                if resultaat:
                    print(f"Priemgetallen tot en met {n}: {resultaat}")
                else:
                    print("Geen priemgetallen gevonden.")
            except ValueError:
                print("Ongeldige invoer! Voer een getal in.")

        elif keuze == "2":
            try:
                n = int(input("Hoeveel priemgetallen wil je? "))
                if n < 1:
                    print("Aantal moet minimaal 1 zijn.")
                else:
                    print(f"De eerste {n} priemgetallen: {first_n_primes(n)}")
            except ValueError:
                print("Ongeldige invoer! Voer een getal in.")

        elif keuze == "3":
            try:
                start = int(input("Eerste getal van de reeks: "))
                end = int(input("Laatste getal van de reeks: "))
                if start > end:
                    print("Het eerste getal moet kleiner of gelijk zijn aan het tweede getal.")
                else:
                    resultaat = primes_between(start, end)
                    if resultaat:
                        print(f"Priemgetallen tussen {start} en {end}: {resultaat}")
                    else:
                        print("Geen priemgetallen gevonden in dit bereik.")
            except ValueError:
                print("Ongeldige invoer! Voer een getal in.")

        elif keuze == "4":
            print("Programma afgesloten.")
            break

        else:
            print("Ongeldige keuze, probeer opnieuw.")


if __name__ == "__main__":
    main()
