import random
from lingowords import words
from ballenbak import ballenbak, grabbelen

rode_ballen = 0
groene_ballen = 0
woorden_goedgekeurd = 0  
def update_ballen(bal):
    global rode_ballen, groene_ballen
    if bal == "rood":
        rode_ballen += 1
    elif bal == "groen":
        groene_ballen += 1

while True:
    gekozen_woord = random.choice(words)
    huidige_status = gekozen_woord[0] + "_" * (len(gekozen_woord)-1)
    pogingen = 5

    print("\nNieuw woord!")
    print("Beginletter is:", gekozen_woord[0])

    for poging in range(pogingen):
        print("Huidige status:", huidige_status)
        gok = input("Doe een gok: ")

        if len(gok) != len(gekozen_woord):
            print("Woord moet", len(gekozen_woord), "letters hebben")
            continue

        if gok == gekozen_woord:
            print("Goed geraden!!")
            woorden_goedgekeurd += 1
            bal1, bal2 = grabbelen(ballenbak)
            print("Eerste bal:", bal1)
            update_ballen(bal1)
            if bal2:
                print("Tweede bal:", bal2)
                update_ballen(bal2)
            else:
                print("Geen tweede bal, eerste bal was rood")

            break 
        else:
            resultaat = ""
            for i in range(len(gekozen_woord)):
                if gok[i] == gekozen_woord[i]:
                    resultaat += "🟢" + gok[i]
                    huidige_status = huidige_status[:i] + gok[i] + huidige_status[i+1:]
                elif gok[i] in gekozen_woord:
                    resultaat += "🟡" + gok[i]
                else:
                    resultaat += "⬜" + gok[i]
            print(resultaat)
    else:
        print("Maximaal aantal pogingen bereikt. Het woord was:", gekozen_woord)

    if rode_ballen >= 3:
        print("Team heeft verloren door 3 rode ballen!")
        break
    if groene_ballen >= 3:
        print("Team wint door 3 groene ballen!")
        break
    if woorden_goedgekeurd >= 10:
        print("Team wint door 10 goed geraden woorden!")
        break

    opnieuw = input("Wil je nog een woord raden? (ja/nee): ")
    if opnieuw.lower() != "ja":
        print("Einde spel!")
        break