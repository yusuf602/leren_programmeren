import random
from lingowords import words

pogingen = 5

gekozen_woord =  random.choice(words)

huidige_status = gekozen_woord[0] + "_" * (len(gekozen_woord)-1)

print (huidige_status)
for pogingen in range(pogingen):
    gok = input("doe een gok: ")

    if gok == gekozen_woord:
        print(f"goed geraden het woord was {gekozen_woord}")
        break
    else:
        resultaat = ""
        for i in range(len(gekozen_woord)):
            if gok[i] == gekozen_woord[i]:
                resultaat += "🟢"
            elif gok[i] in gekozen_woord:
                resultaat += "🟡"
            else:
                resultaat += "⬜"
        print(resultaat)