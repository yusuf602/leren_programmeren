import random
from ballenbak import maak_ballenbak, grabbelen
from lingowords import words  

pogingen_per_woord = 5
rode_ballen = 0
groene_ballen = 0
woorden_goed = 0
aantal_woorden_fout = 0

ballenbak = maak_ballenbak()

while True:
    gekozen_woord = random.choice(words)
    huidige_status = gekozen_woord[0] + "_" * (len(gekozen_woord) - 1)

    print("Nieuw woord!")
    print("Beginletter is:", gekozen_woord[0])

    for poging in range(pogingen_per_woord):
        print("Huidige status:", huidige_status)

        while True:
            gok = input("Doe een gok: ").lower()

            if len(gok) != len(gekozen_woord):
                print(f"Fout! Het woord moet {len(gekozen_woord)} letters hebben.")
                continue

            break  

        if gok == gekozen_woord:
            print(f"Goed geraden!! Het woord was: {gekozen_woord}")
            woorden_goed += 1
            aantal_woorden_fout = 0

            bal1, bal2 = grabbelen(ballenbak)
            print("Eerste bal:", bal1)

            if bal1 == "rood":
                rode_ballen += 1
                print("Geen tweede bal, eerste was rood")
            else:
                if bal1 == "groen":
                    groene_ballen += 1
                print("Tweede bal:", bal2)
                if bal2 == "rood":
                    rode_ballen += 1
                elif bal2 == "groen":
                    groene_ballen += 1

            break

        else:
            resultaat = ["⬜"] * len(gekozen_woord)
            woord_over = list(gekozen_woord)

            for i in range(len(gekozen_woord)):
                if gok[i] == gekozen_woord[i]:
                    resultaat[i] = "🟢"
                    woord_over[i] = None
                    huidige_status = huidige_status[:i] + gok[i] + huidige_status[i+1:]

            for i in range(len(gekozen_woord)):
                if resultaat[i] == "⬜" and gok[i] in woord_over:
                    resultaat[i] = "🟡"
                    woord_over[woord_over.index(gok[i])] = None

            print("".join(resultaat))

    else:
        print("Maximaal aantal pogingen bereikt. Het woord was:", gekozen_woord)
        aantal_woorden_fout += 1

    print("Score:")
    print("Groene ballen:", groene_ballen)
    print("Rode ballen:", rode_ballen)
    print("Goed geraden woorden:", woorden_goed)

    if rode_ballen >= 3:
        print("Team heeft verloren door 3 rode ballen!")
        break
    if groene_ballen >= 3:
        print("Team wint door 3 groene ballen!")
        break
    if woorden_goed >= 10:
        print("Team wint door 10 goed geraden woorden!")
        break
    if aantal_woorden_fout >= 3:
        print("Jammer, verloren door 3 fout geraden woorden achter elkaar!")
        break

    opnieuw = input("Wil je nog een woord raden? (ja/nee): ").lower()
    if opnieuw != "ja":
        print("Einde spel!")
        break