import random

from ballenbak import maak_ballenbak, grabbelen, tel_speciale_ballen
from lingowords import words


POGINGEN_PER_WOORD = 5
MAX_RODE_BALLEN = 3
MAX_GROENE_BALLEN = 3
MAX_GOED_GERADEN_WOORDEN = 10
MAX_FOUTE_WOORDEN_OP_RIJ = 3


def vraag_gok(gekozen_woord):
    while True:
        gok = input("Doe een gok: ").strip().lower()

        if len(gok) != len(gekozen_woord):
            print(f"Fout! Het woord moet {len(gekozen_woord)} letters hebben.")
            continue

        if not gok.isalpha():
            print("Fout! Gebruik alleen letters.")
            continue

        return gok


def controleer_gok(gok, gekozen_woord, huidige_status):
    resultaat = ["."] * len(gekozen_woord)
    woord_over = list(gekozen_woord)

    for i in range(len(gekozen_woord)):
        if gok[i] == gekozen_woord[i]:
            resultaat[i] = "G"
            woord_over[i] = None
            huidige_status = huidige_status[:i] + gok[i] + huidige_status[i + 1:]

    for i in range(len(gekozen_woord)):
        if resultaat[i] == "." and gok[i] in woord_over:
            resultaat[i] = "Y"
            woord_over[woord_over.index(gok[i])] = None

    return resultaat, huidige_status


def speel_woord(gekozen_woord):
    huidige_status = gekozen_woord[0] + "_" * (len(gekozen_woord) - 1)

    print("\nNieuw woord!")
    print("Beginletter is:", gekozen_woord[0])

    for poging in range(1, POGINGEN_PER_WOORD + 1):
        print(f"\nPoging {poging}/{POGINGEN_PER_WOORD}")
        print("Huidige status:", huidige_status)

        gok = vraag_gok(gekozen_woord)

        if gok == gekozen_woord:
            print(f"Goed geraden! Het woord was: {gekozen_woord}")
            return True

        resultaat, huidige_status = controleer_gok(gok, gekozen_woord, huidige_status)
        print("Resultaat:", " ".join(resultaat))
        print("G = juiste plek, Y = zit in het woord, . = fout")

    print("Maximaal aantal pogingen bereikt. Het woord was:", gekozen_woord)
    return False


def toon_score(groene_ballen, rode_ballen, woorden_goed, aantal_woorden_fout):
    print("\nScore:")
    print("Groene ballen:", groene_ballen)
    print("Rode ballen:", rode_ballen)
    print("Goed geraden woorden:", woorden_goed)
    print("Foute woorden op rij:", aantal_woorden_fout)


def spel_is_afgelopen(groene_ballen, rode_ballen, woorden_goed, aantal_woorden_fout):
    if rode_ballen >= MAX_RODE_BALLEN:
        print("Team heeft verloren door 3 rode ballen!")
        return True

    if groene_ballen >= MAX_GROENE_BALLEN:
        print("Team wint door 3 groene ballen!")
        return True

    if woorden_goed >= MAX_GOED_GERADEN_WOORDEN:
        print("Team wint door 10 goed geraden woorden!")
        return True

    if aantal_woorden_fout >= MAX_FOUTE_WOORDEN_OP_RIJ:
        print("Jammer, verloren door 3 fout geraden woorden achter elkaar!")
        return True

    return False


def speel_lingo():
    rode_ballen = 0
    groene_ballen = 0
    woorden_goed = 0
    aantal_woorden_fout = 0
    ballenbak = maak_ballenbak()

    while True:
        gekozen_woord = random.choice(words)
        goed_geraden = speel_woord(gekozen_woord)

        if goed_geraden:
            woorden_goed += 1
            aantal_woorden_fout = 0

            bal1, bal2 = grabbelen(ballenbak)
            getrokken_ballen = [bal for bal in [bal1, bal2] if bal is not None]
            extra_rood, extra_groen = tel_speciale_ballen(getrokken_ballen)
            rode_ballen += extra_rood
            groene_ballen += extra_groen

            print("Getrokken ballen:", getrokken_ballen)
        else:
            aantal_woorden_fout += 1

        toon_score(groene_ballen, rode_ballen, woorden_goed, aantal_woorden_fout)

        if spel_is_afgelopen(groene_ballen, rode_ballen, woorden_goed, aantal_woorden_fout):
            break

        opnieuw = input("\nWil je nog een woord raden? (ja/nee): ").strip().lower()
        if opnieuw != "ja":
            print("Einde spel!")
            break


if __name__ == "__main__":
    speel_lingo()