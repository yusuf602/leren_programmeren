import random

# Deck genereren
kleuren = ["Harten", "Klaveren", "Schoppen", "Ruiten"]
waarden = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Boer", "Vrouw", "Heer", "Aas"]
deck = [f"{kleur} van {waarde}" for kleur in kleuren for waarde in waarden] + ["Joker", "Joker"]

random.shuffle(deck)
getrokken_kaarten = deck[:7]
overgebleven_kaarten = deck[7:]

# Resultaat 
print(f"Getrokken kaarten ({len(getrokken_kaarten)}): {getrokken_kaarten}")
for i, kaart in enumerate(getrokken_kaarten, start=1):
    print(f"{i} kaart: {kaart}")
print('')
print(f"Overgebleven kaarten ({len(overgebleven_kaarten)}): {overgebleven_kaarten}")
