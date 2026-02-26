from time import sleep

sleutel = False
speeltje = False

def game_over():
    print("GAME OVER")
    exit()

def win():
    print("32mJE BENT ONTSNAPT!")
    exit()

def start():
    print("Je bent in slaap gevallen op school...")
    sleep(2)
    print("Je wordt wakker in het donker.")
    sleep(2)
    print("Iedereen is weg en het alarm staat aan!")
    sleep(2)
    print("Je moet hier zien uit te komen, anders krijg je een schorsing door poging tot inbraak!")
    klaslokaal()

def klaslokaal():
    global sleutel
    print("-- KLASLOKAAL ---")
    print("Je ziet een sleutel op het bureau en 2 deuren.")

    keuze = input("A) Pak sleutel  B) Laat sleutel liggen: ")

    if keuze.lower() == "a":
        sleutel = True
        print("Je pakt de sleutel.")
    else:
        print("Je laat de sleutel liggen.")

    deur = input("A) Linker deur  B) Rechter deur: ")

    if deur.lower() == "a":
        grote_hal()
    else:
        controlekamer()

def grote_hal():
    print("--- GROTE HAL ---")
    print("Camera's hangen overal.")

    keuze = input("A) Doorlopen  B) Terug. ")

    if keuze.lower() == "a":
        print("Camera zag je! Alarm!")
        game_over()
    else:
        klaslokaal()

def controlekamer():
    global speeltje
    print("--- CONTROLEKAMER ---")
    print("Je ziet een kast.")

    keuze = input("A) Kast openen  B) Negeren: ")

    if keuze.lower() == "a":
        print("Je vindt een hondenspeeltje!")
        neem = input("Neem je het mee? ja/nee: ")

        if neem.lower() == "ja":
            speeltje = True
            print("Je stopt het speeltje in je tas.")
    sleep(2)
    print("je loopt richting de aula")
    sleep(2)
    print("doordat je in de cotrole kamer zat zag je via de camera dat de bwaker hier te vinden is.")
    sleep(2)
    print("je moet hem zien te ontwijken")
    sleep(2)
    print("je ziet een hond met hem.")
    sleep(2)

    aula()

def aula():
    print("--- AULA ---")
    print("De bewaker en hond zien je!")

    if speeltje:
        keuze = input("A) Gooi speeltje  B) Rennen: ")

        if keuze.lower() == "a":
            print("De hond rent weg!")
            print("De bewaker rent achter de hond aan!")
            nooduitgang()
        else:
            print("De bewaker pakt je.")
            game_over()
    else:
        print("Je hebt geen speeltje. De hond pakt je.")
        game_over()

def nooduitgang():
    print("--- NOODUITGANG ---")

    if sleutel:
        print("Je opent de deur met de sleutel!")
        win()
    else:
        print("De deur zit op slot. Je hebt geen sleutel.")
        game_over()

start()
