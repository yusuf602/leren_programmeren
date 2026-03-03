import functies

print("Welkom bij Papi Gelato!")
print("Hier kunt u direct uw ijsjes verkopen.\n")

while True: 
    while True:
        klant_type = input("Bent u 1) een particuliere klant of 2) een zakelijke klant? ")
        if klant_type in ["1","2"]:
            break
        else:
            print("Sorry dat snap ik niet...")

    if klant_type == "1":
        bestellingen = []

        while True:
            aantal = functies.vraag_aantal_bolletjes()
            smaken = functies.vraag_smaak_per_bolletje(aantal)
            keuze = functies.vraag_bakje_of_hoorntje(aantal)
            topping = functies.vraag_topping(aantal, keuze)

            bestelling = {
                "smaken": smaken,
                "keuze": keuze,
                "topping": topping
            }
            bestellingen.append(bestelling)

            nog_een = functies.vraag_nog_een_bestelling()
            if nog_een == "nee":
                print("Ronde afgerond!")
                break

        functies.print_bon(bestellingen)

    else:
        functies.zakelijke_bestelling()

    input("\nDruk op Enter voor de volgende klant...")
    print("\n--- Nieuwe klant ---\n")