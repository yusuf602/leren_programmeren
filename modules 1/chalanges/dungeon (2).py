import random
import time
import math

# Spelers eigenschappen
player_attack = 1
player_defense = 0
player_health = 3
rupees = 0
heeft_sleutel = False

# === [Vechtfunctie] === #
def vecht_met_vijand(vijand_naam, vijand_attack, vijand_defense, vijand_health):
    """
    Generieke functie voor het vechten met een vijand.
    """
    global player_health
    print(f"Je wordt geconfronteerd met een {vijand_naam}!")

    vijand_hit_damage = max(0, vijand_attack - player_defense)
    if vijand_hit_damage == 0:
        print(f"De {vijand_naam} kan je geen schade doen dankzij je verdediging. Je gaat verder.\n")
        return True

    vijand_attack_amount = math.ceil(player_health / vijand_hit_damage)
    player_hit_damage = max(0, player_attack - vijand_defense)

    if player_hit_damage == 0:
        print(f"Je kunt geen schade doen aan de {vijand_naam}. De {vijand_naam} wint.")
        print("Game over.")
        exit()

    player_attack_amount = math.ceil(vijand_health / player_hit_damage)

    if player_attack_amount <= vijand_attack_amount:
        print(f"In {player_attack_amount} rondes versla je de {vijand_naam}.")
        player_health = max(0, player_health - vijand_attack_amount * vijand_hit_damage)
        print(f"Je health is nu {player_health}.\n")
        return True
    else:
        print(f"Helaas is de {vijand_naam} te sterk voor je.")
        print("Game over.")
        exit()

# === [kamer 1] === #
def kamer1():
    print('Door de twee grote deuren loop je een gang binnen.')
    print('Het ruikt hier muf en vochtig.')
    print('Je ziet een deur voor je. Je hart klopt in je keel.\n')
    time.sleep(2)
    kamer2()

# === [kamer 2] === #
def kamer2():
    global rupees
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Op zijn borst zit een numpad met de toetsen 9 t/m 0.')

    while True:
        getal1 = random.randint(10, 25)
        getal2 = random.randint(-5, 75)
        operator = random.choice(['+', '-', '*'])

        if operator == '+':
            uitkomst = getal1 + getal2
        elif operator == '-':
            uitkomst = getal1 - getal2
        elif operator == '*':
            uitkomst = getal1 * getal2

        print(f'Daarboven zie je een som staan: {getal1} {operator} {getal2} = ?')

        try:
            antwoord = int(input('Wat is je antwoord? (typ een getal): '))
        except ValueError:
            print('Dat is geen geldig nummer. Probeer opnieuw.\n')
            continue

        if antwoord == uitkomst:
            print('Correct! Je ontvangt een rupee van het standbeeld.')
            rupees += 1
            break
        else:
            print(f'Onjuist. De juiste uitkomst was {uitkomst}. Probeer opnieuw.\n')

    kamer9()

# === [kamer 8] === #
def kamer8():
    print("Je komt een kamer binnen met een gokmachine in het midden.")
    print("Wil je je geluk beproeven?")
    keuze = input("Typ 'ja' om te gokken of 'nee' om door te gaan: ").lower()

    if keuze == "ja":
        gokmachine()
    print("Je verlaat de gokmachine en gaat verder.\n")
    
    # Optie om naar kamer 3 te gaan
    keuze = input("Wil je naar kamer 3 gaan? Typ 'ja' om naar kamer 3 te gaan of 'nee' om verder te gaan naar kamer 9: ").lower()
    if keuze == "ja":
        kamer3()
    else:
        kamer9()

def gokmachine():
    global rupees, player_health
    print("Je trekt aan de hendel van de gokmachine...\n")
    time.sleep(2)
    dobbel1 = random.randint(1, 6)
    dobbel2 = random.randint(1, 6)
    totaal = dobbel1 + dobbel2
    print(f"De dobbelstenen rollen: {dobbel1} en {dobbel2} (totaal: {totaal}).")

    if totaal > 7:
        rupees *= 2
        print(f"Gefeliciteerd! Je rupees zijn verdubbeld. Je hebt nu {rupees} rupee(s).\n")
    elif totaal < 7:
        player_health -= 1
        print("Helaas, je verloor 1 health.")
        print(f"Je gezondheid is nu {player_health}.\n")
        if player_health <= 0:
            print("Je gezondheid is 0. Game over.")
            exit()
    else:  # totaal == 7
        rupees += 1
        player_health = min(3, player_health + 4)  # Max health is 3
        print("Geweldig! Je hebt 1 rupee gewonnen en je gezondheid volledig hersteld.")
        print(f"Je hebt nu {rupees} rupee(s) en {player_health} gezondheid.\n")

# === [kamer 9] === #
def kamer9():
    global player_defense, player_health
    print("Je komt in een betoverde kamer.")
    betovering = random.choice(["defense", "health"])

    if betovering == "defense":
        player_defense += 1
        print("Je voelt je sterker en je verdediging is met 1 toegenomen!")
    elif betovering == "health":
        player_health = min(3, player_health + 2)  # Max health is 3
        print("Je voelt je gezonder en je gezondheid is met 2 toegenomen!")
    print(f"Je huidige stats: aanval {player_attack}, verdediging {player_defense}, gezondheid {player_health}\n")
    
    # Optie om naar kamer 3 te gaan
    keuze = input("Wil je naar kamer 3 gaan? Typ 'ja' om naar kamer 3 te gaan of 'nee' om verder te gaan naar kamer 7: ").lower()
    if keuze == "ja":
        kamer3()
    else:
        kamer7()

# === [kamer 3] === #
def kamer3():
    global rupees
    print('Je stapt een kamer binnen en ziet een kleine goblin achter een balie staan.')
    print('"Welkom bij mijn winkel!" roept de goblin.')

    winkel_items = {
        "1": ("schild", "verhoogt je verdediging met 1", lambda: increase_stat("defense", 1)),
        "2": ("zwaard", "verhoogt je aanval met 2", lambda: increase_stat("attack", 2)),
        "3": ("sleutel", "nodig om de schatkist te openen", lambda: koop_sleutel()),
    }

    while True:
        print(f"\nJe hebt {rupees} rupee(s). Dit zijn de items die je kunt kopen:")
        for key, (naam, beschrijving, _) in winkel_items.items():
            print(f"{key}: {naam} - {beschrijving} (1 rupee)")
        print("4: Verlaat de winkel")
        keuze = input("Wat wil je kopen? (typ een nummer): ")

        if keuze in winkel_items and rupees > 0:
            rupees -= 1
            winkel_items[keuze][2]()  # Roep de functie aan die het item-effect toepast
            print(f"Je hebt een {winkel_items[keuze][0]} gekocht!")
            print(f"Je hebt nu {rupees} rupee(s) over.\n")
        elif keuze == "4":
            print("Je verlaat de winkel en gaat verder.\n")
            kamer4()
            break
        else:
            print("Onbekende keuze of niet genoeg rupees. Probeer opnieuw.\n")

def increase_stat(stat, amount):
    global player_attack, player_defense, player_health
    if stat == "attack":
        player_attack += amount
    elif stat == "defense":
        player_defense += amount
    elif stat == "health":
        player_health = min(3, player_health + amount)

def koop_sleutel():
    global heeft_sleutel
    heeft_sleutel = True
    print("Je hebt een sleutel gekocht!")

# === [kamer 7] === #
def kamer7():
    global rupees
    print("Je loopt een kamer binnen en kijkt om je heen.")
    if random.randint(1, 10) != 1:
        print("Je vindt een rupee op de grond en steekt deze in je zak.")
        rupees += 1
    else:
        print("De kamer is leeg. Er ligt geen rupee.\n")
    kamer8()

# === [kamer 4] === #
def kamer4():
    print("Je komt in een nieuwe kamer, deze lijkt leeg te zijn...")
    # Hier kan je verdergaan met het spel

kamer1()  # Start het spel
