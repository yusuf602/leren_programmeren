wachtwoord = 'honden'
gok = 0
limiet = 5

while gok < limiet:
    kans = input('Wachtwoord?: ')

    if kans == wachtwoord:
        print(f'Gefeliciteerd, je hebt het wachtwoord geraden. met {gok} pogingen.')
        break  
    gok += 1  
    print(f'Poging {gok} van {limiet}.')  
if kans != wachtwoord:
    print('u mag niet meer inloggen!')

