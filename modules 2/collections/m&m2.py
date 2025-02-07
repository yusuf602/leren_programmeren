import random

kleuren = ['rood', 'blauw', 'groen', 'geel', 'bruin']

aantal_mms = int(input("Hoeveel M&M's wilt u toevoegen aan de zak? "))

zak = {}

# Vul de zak met willekeurige aantallen M&M's per kleur
for kleur in kleuren:
    # Willekeurig aantal M&M's per kleur, van 0 tot het opgegeven aantal M&M's
    aantal_kleur = random.randint(0, aantal_mms)
    # Voeg de kleur en het aantal M&M's alleen toe als het aantal groter is dan 0
    if aantal_kleur > 0:
        zak[kleur] = aantal_kleur

# Print de zak met M&M's
print("Zak met M&M's:")
for kleur, aantal in zak.items():
    print(f"{kleur}: {aantal}")
