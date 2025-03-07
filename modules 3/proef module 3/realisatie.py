import random

deelnemers = []
while len(deelnemers) < 3:
    naam = input ('voer een unieke naam in: ').lower()
    if naam in deelnemers:
        print('deze naam is al in gebruik, probeer een andere naam.')
    else:
        deelnemers.append(naam)
while True:
    keuze = input("Wil je nog een naam toevoegen? (ja/nee): ").strip().lower()
    if keuze == "ja":
        naam = input("Voer een unieke naam in: ").strip()
        if naam in deelnemers:
            print("Deze naam is al ingevoerd, probeer een andere.")
        elif naam:
            deelnemers.append(naam)
        else:
            print("Ongeldige invoer, probeer opnieuw.")
    elif keuze == "nee":
        break
    else:
        print("Ongeldige keuze, typ 'ja' of 'nee'.")
lootjes = deelnemers[:]  
random.shuffle(lootjes)  

while any(deelnemers[i] == lootjes[i] for i in range(len(deelnemers))):  
    random.shuffle(lootjes)  

for i in range(len(deelnemers)):  
    print(f"{deelnemers[i]} heeft {lootjes[i]} als lootje getrokken.")  

