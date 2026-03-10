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
        print("helaas fout")
