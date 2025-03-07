boodschappenlijst = {}

while True:
    artikel = input("Welk artikel wilt u toevoegen? ").strip().lower()
    
    while True:
        try:
            aantal = int(input(f"Hoeveel '{artikel}' wilt u toevoegen? "))
            if aantal > 0:
                break
            else:
                print("Voer een positief getal in.")
        except ValueError:
            print("Voer een geldig getal in.")

    if artikel in boodschappenlijst:
        boodschappenlijst[artikel] += aantal
    else:
        boodschappenlijst[artikel] = aantal

    verder = input("Wilt u nog meer boodschappen toevoegen? (ja/nee) ").strip().lower()
    if verder != 'ja':
        break

print("\nUw boodschappenlijst:")
for item, hoeveelheid in boodschappenlijst.items():
    print(f"- {item.capitalize()}: {hoeveelheid}x")
