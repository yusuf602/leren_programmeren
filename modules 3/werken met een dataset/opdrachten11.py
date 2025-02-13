from fruitmand import fruitmand

# Verzamel de beschikbare kleuren
beschikbare_kleuren = {fruit['color'] for fruit in fruitmand}

# Vraag om een geldige kleur
while True:
    kleur = input(f"Kies een kleur uit {beschikbare_kleuren}: ").lower()
    if kleur in beschikbare_kleuren:
        break
    print(f"De kleur {kleur} zit er niet in de fruitmand")

rond = sum(1 for fruit in fruitmand if fruit['color'] == kleur and fruit['round'])
niet_rond = sum(1 for fruit in fruitmand if fruit['color'] == kleur and not fruit['round'])

verschil = abs(rond - niet_rond)
if rond > niet_rond:
    print(f"Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
elif niet_rond > rond:
    print(f"Er zijn {verschil} minder ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
else:
    print(f"Er zijn {rond} ronde vruchten en {niet_rond} niet ronde vruchten in de kleur {kleur}")
