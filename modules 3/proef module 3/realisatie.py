import random


deelnemers = []

while len(deelnemers) < 3:
    naam = input("Voer een unieke naam in: ").strip().lower()
    if naam in deelnemers:
        print("Deze naam is al in gebruik, probeer een andere.")
    elif naam:
        deelnemers.append(naam)

while True:
    keuze = input("Wil je nog een naam toevoegen? (ja/nee): ").strip().lower()
    if keuze == "ja":
        naam = input("Voer een unieke naam in: ").strip().lower()
        if naam in deelnemers:
            print("Deze naam is al ingevoerd, probeer een andere.")
        elif naam:
            deelnemers.append(naam)
    elif keuze == "nee":
        break
    else:
        print("Ongeldige keuze, typ 'ja' of 'nee'.")
    
lootjes = deelnemers[:]  
while True:
    random.shuffle(lootjes)
    if all(deelnemers[i] != lootjes[i] for i in range(len(deelnemers))):
        break 

verdeling = {deelnemers[i]: lootjes[i] for i in range(len(deelnemers))}

print("Alle lootjes zijn getrokken! Voer je naam in om te zien wie je hebt.")
    
while True:
    naam = input("Voer je naam in (of typ 'stop' om te stoppen): ").strip().lower()
    if naam == "stop":
        break
    elif naam in verdeling:
        print(f"{naam}, jij hebt {verdeling[naam]} getrokken!")
    else:
        print("Deze naam zit niet in de lijst. Probeer opnieuw.")

