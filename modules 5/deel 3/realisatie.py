import random
deelnemers = []

while len(deelnemers) < 3:
    naam = input("Voer een unieke naam in: ").strip().lower()
    if any(d['naam'] == naam for d in deelnemers):  # aangepast voor dict check
        print("Deze naam is al in gebruik, probeer een andere.")
    elif naam:
        cadeaus = []
        print("Noem drie cadeautjes die je graag wilt ontvangen:")
        for i in range(3):
            cadeau = input(f"Cadeau {i+1}: ")
            cadeaus.append(cadeau)
        deelnemers.append({'naam': naam, 'cadeaus': cadeaus})

while True:
    keuze = input("Wil je nog een naam toevoegen? (ja/nee): ").strip().lower()
    if keuze == "ja":
        naam = input("Voer een unieke naam in: ").strip().lower()
        if any(d['naam'] == naam for d in deelnemers):
            print("Deze naam is al ingevoerd, probeer een andere.")
        elif naam:
            cadeaus = []
            print("Noem drie cadeautjes die je graag wilt ontvangen:")
            for i in range(3):
                cadeau = input(f"Cadeau {i+1}: ")
                cadeaus.append(cadeau)
            deelnemers.append({'naam': naam, 'cadeaus': cadeaus})
    elif keuze == "nee":
        break
    else:
        print("Ongeldige keuze, typ 'ja' of 'nee'.")

namen = [d['naam'] for d in deelnemers] 
lootjes = namen[:]
while True:
    random.shuffle(lootjes)
    if all(namen[i] != lootjes[i] for i in range(len(namen))):
        break 

verdeling = {namen[i]: lootjes[i] for i in range(len(namen))}

print("Alle lootjes zijn getrokken! Voer je naam in om te zien wie je hebt.")

while True:
    naam = input("Voer je naam in (of typ 'stop' om te stoppen): ").strip().lower()
    if naam == "stop":
        break
    elif naam in verdeling:
        print(f"{naam}, jij hebt {verdeling[naam]} getrokken!")
    else:
        print("Deze naam zit niet in de lijst. Probeer opnieuw.")

print("\nOverzicht van alle deelnemers en hun cadeautjes:")
for d in deelnemers:
    print(f"{['naam']}: {', '.join(['cadeaus'])}")
