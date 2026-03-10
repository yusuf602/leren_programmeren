import random
from lingowords import words

gekozen_woord =  random.choice(words)

huidige_status = gekozen_woord[0] + "_" * (len(gekozen_woord)-1)

print("beginletter", gekozen_woord[0])
print (huidige_status)