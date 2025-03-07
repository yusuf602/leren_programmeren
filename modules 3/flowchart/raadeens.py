import random

def raadspel():
    max_ronden = 20
    max_beurten = 10
    score = 0
    
    print("Welkom bij het Raadspel!")
    
    for ronde in range(1, max_ronden + 1):
        geheim_getal = random.randint(1, 1000)
        print(f"\nRonde {ronde}: Raad het geheime getal (tussen 1 en 1000)")
        
        for beurt in range(1, max_beurten + 1):
            try:
                gok = int(input(f"Beurt {beurt}: Jouw gok: "))
            except ValueError:
                print("Ongeldige invoer, voer een getal in.")
                continue

            verschil = abs(gok - geheim_getal)
            
            if verschil == 0:
                print("Gefeliciteerd! Je hebt het getal geraden!")
                score += 1
                break
            elif verschil <= 20:
                print("Je bent heel warm!")
            elif verschil <= 50:
                print("Je bent warm!")
                
            if gok < geheim_getal:
                print("Te laag!")
            else:
                print("Te hoog!")
        
        print(f"Ronde afgelopen. Huidige score: {score}")
        
        if ronde < max_ronden:
            doorgaan = input("Nog een getal raden? (ja/nee): ").strip().lower()
            if doorgaan != "ja":
                break
    
    print(f"\nSpel afgelopen! Jouw eindscore is: {score} punten.")

raadspel()
