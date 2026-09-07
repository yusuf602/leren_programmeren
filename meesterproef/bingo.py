def maak_bingokaart():
    nummers = list(range(1, 17))

    kaart = []

    for i in range(0, 16, 4):
        rij = nummers[i:i + 4]
        kaart.append(rij)

    return kaart


def toon_bingokaart(kaart):
    print("\nBingokaart:")

    for rij in kaart:
        print(" ".join(
            f"{nummer:2}" if nummer != 0 else " X"
            for nummer in rij
        ))


def streep_nummer_door(kaart, nummer):
    for rij in range(4):
        for kolom in range(4):
            if kaart[rij][kolom] == nummer:
                kaart[rij][kolom] = 0
                return True

    return False


def heeft_lijn(kaart):
    # Horizontale lijnen
    for rij in kaart:
        if all(vakje == 0 for vakje in rij):
            return True

    # Verticale lijnen
    for kolom in range(4):
        if all(kaart[rij][kolom] == 0 for rij in range(4)):
            return True

    # Diagonale lijn van linksboven naar rechtsonder
    if all(kaart[i][i] == 0 for i in range(4)):
        return True

    # Diagonale lijn van rechtsboven naar linksonder
    if all(kaart[i][3 - i] == 0 for i in range(4)):
        return True

    return False

if __name__ == "__main__":
    kaart = maak_bingokaart()

    toon_bingokaart(kaart)

    # Test een horizontale lijn
    for nummer in [1, 2, 3, 4]:
        streep_nummer_door(kaart, nummer)

    print("\nNa het trekken van 1, 2, 3 en 4:")
    toon_bingokaart(kaart)

    if heeft_lijn(kaart):
        print("BINGO! Er is een lijn.")
    else:
        print("Nog geen bingo.")