import random
from lingowords import words

pogingen = 5

print("nieuw beginletter is")

gekozen_woord =  random.choice(words)

huidige_status = gekozen_woord[0] + "_" * (len(gekozen_woord)-1)

print (huidige_status)
for poging in range(pogingen):
    print (huidige_status)

    gok = input("doe een gok: ")
    print(gekozen_woord)
    if gok == gekozen_woord:
        print(f"goed geraden het woord was", gekozen_woord)
        break
    else:
        resultaat = ""
        for i in range(len(gekozen_woord)):
            if gok[i] == gekozen_woord[i]:
                resultaat += "🟢"
                huidige_status = huidige_status[:i] + gok[i] + huidige_status[i+1:]
            elif gok[i] in gekozen_woord:
                resultaat += "🟡"
            else:
                resultaat += "⬜"
        print(resultaat)

else:
    print("maximaal aantal pogingen bereik")
    print("het woord was", gekozen_woord)