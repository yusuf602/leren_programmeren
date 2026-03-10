import data

def vraag_aantal_bolletjes():
    while True:
        aantal = input("Hoeveel bolletjes wilt u? ")
        if not aantal.isdigit():
            print("Invoer niet begrepen.")
            continue
        aantal = int(aantal)
        if aantal < data.MIN_BOLLETJES:
            print("Invoer niet begrepen.")
        elif aantal > data.MAX_BOLLETJES:
            print("Zulke grote bakken zijn niet mogelijk.")
        else:
            return aantal

def vraag_smaak_per_bolletje(aantal):
    smakenlijst = []
    for i in range(1, aantal + 1):
        while True:
            keuze = input(f"Welke smaak wilt u voor bolletje nummer {i}? A) Aardbei, C) Chocoladeof V) Vanille? ").upper()
            if keuze in data.SMAKEN:
                smakenlijst.append(keuze)
                break
            else:
                print("Sorry dat snap ik niet...")
    return smakenlijst

def vraag_bakje_of_hoorntje(aantal):
    if aantal > data.MAX_HOORNTJE:
        print("Voor meer dan 3 bolletjes krijgt u automatisch een bakje.")
        return "bakje"
    while True:
        keuze = input("Wilt u een hoorntje of een bakje? ").lower()
        if keuze not in data.GELDIGE_BAKJES:
            print("Invoer niet begrepen.")
        else:
            return keuze

def vraag_topping(aantal, keuze_bakje):
    while True:
        topping = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ").upper()
        if topping in data.TOPPINGS:
            return topping
        else:
            print("Sorry dat snap ik niet...")

def vraag_nog_een_bestelling():
    while True:
        antwoord = input("Wilt u nog meer bestellen? (ja/nee) ").lower()
        if antwoord in data.GELDIGE_ANTWOORDEN:
            return antwoord
        else:
            print("Invoer niet begrepen.")

def bereken_topping_prijs(topping, aantal, keuze_bakje):
    if topping == "A":
        return 0
    elif topping == "B":
        return data.PRIJS_TOPPINGS["B"]
    elif topping == "C":
        return data.PRIJS_TOPPINGS["C"] * aantal
    elif topping == "D":
        return data.PRIJS_TOPPINGS["D"][0] if keuze_bakje == "hoorntje" else data.PRIJS_TOPPINGS["D"][1]

def print_bon(bestellingen):
    print("\n-----------BON-----------")
    totaal_prijs = 0

    for bestelling in bestellingen:
        smaken = bestelling["smaken"]
        for smaak in smaken:
            print(f"1 bolletje {data.SMAKEN[smaak]}  €{data.PRIJS_BOLLETJE:.2f}")
            totaal_prijs += data.PRIJS_BOLLETJE

        if bestelling["keuze"] == "hoorntje":
            print(f"1 hoorntje  €{data.PRIJS_HOORNTJE:.2f}")
            totaal_prijs += data.PRIJS_HOORNTJE
        else:
            print(f"1 bakje  €{data.PRIJS_BAKJE:.2f}")
            totaal_prijs += data.PRIJS_BAKJE

        topping = bestelling["topping"]
        if topping != "A":
            prijs_topping = bereken_topping_prijs(topping, len(smaken), bestelling["keuze"])
            print(f"Topping: {data.TOPPINGS[topping]}  €{prijs_topping:.2f}")
            totaal_prijs += prijs_topping

    print("-----------------")
    print(f"Totaal: € {totaal_prijs:.2f}")

def zakelijke_bestelling():
    while True:
        aantal_liter = input("Hoeveel liter wilt u bestellen? ")
        if aantal_liter.isdigit() and int(aantal_liter) > 0:
            aantal_liter = int(aantal_liter)
            break
        else:
            print("Invoer niet begrepen.")
    
    smakenlijst = []
    for i in range(1, aantal_liter + 1):
        while True:
            smaak = input(f"Welke smaak voor liter {i}? A) Aardbei, C) Chocolade of V) Vanille? ").upper()
            if smaak in data.SMAKEN:
                smakenlijst.append(smaak)
                break
            else:
                print("Sorry dat snap ik niet...")

    totaal = aantal_liter * data.PRIJS_PER_LITER
    btw = totaal * data.BTW_PERCENTAGE / 100
    print("\n------ BON ZAKELIJK ------")
    for smaak in smakenlijst:
        print(f"1 liter {data.SMAKEN[smaak]}  €{data.PRIJS_PER_LITER:.2f}")
    print(f"Totaal: €{totaal:.2f}")
    print(f"BTW {data.BTW_PERCENTAGE}%: €{btw:.2f}")