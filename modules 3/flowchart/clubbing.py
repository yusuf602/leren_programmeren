
PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

def geef_bandje(kleur):
    print(f"Je krijgt van mij een {kleur} bandje")
    return kleur

def geef_drank(drank, prijs=None):
    if prijs:
        print(f"Alsjeblieft je {drank}, dat is dan €{prijs:.2f}")
    else:
        print(f"Alsjeblieft, complimenten van het huis")

leeftijd = int(input("Hoe oud ben je? "))

if leeftijd < 18:
    print("Sorry je mag niet naar binnen")
else:
    naam = input("Wat is je naam? ").strip().lower()
    is_vip = naam in VIP_LIST
    if naam in VIP_LIST:
        
        if leeftijd >= 21:
           bandje = geef_bandje("blauw") 
        else:
            bandje = geef_bandje("rood") 
    else:
        if not is_vip and leeftijd >= 21:
            print("Je krijgt van mij een stempel")

    drankje = input("Wat wil je drinken? ").strip().lower()

    if drankje not in DRANKJES:
        print("Sorry geen idee wat je bedoelt, hier een glaasje water")
    elif drankje == "cola":
        if bandje:
            geef_drank(drankje)
        else:
            geef_drank(drankje, PRIJS_COLA)
    elif drankje == "bier":
        if is_vip:
            if leeftijd >= 18:
                geef_drank(drankje,)
                print("complimenten van het huis")
            else:
                print("Sorry je mag geen alcohol bestellen onder de 21")
        if leeftijd >=21:
            print(f"alsjeblieft je {drankje} dat word dan {PRIJS_BIER} Euro ")
        else:
            print("Sorry je mag geen alcohol bestellen onder de 21")
    elif drankje == "champagne":
        if is_vip:
            geef_drank(drankje, PRIJS_CHAMPAGNE)
        else:
            print("Sorry alleen vips mogen champagne bestellen")

print("Einde programma")
