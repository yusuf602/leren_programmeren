#voornaam, achternaam en opdracht: Pizza calculator
getal1 = int(input('hoeveel small pizza s wilt u? '))
getal2 = int(input('hoeveel medium pizza s wilt u? '))
getal3 = int(input('hoeveel large pizza s wilt u? '))

small = 6.5
medium = 9.30
large = 11.10

antwoord1 = getal1 * small
antwoord2 = getal2 * medium
antwoord3 = getal3 * large
total = antwoord1 + antwoord2 + antwoord3
print('********************KASSA BON*********************')
print(f'pizzas small:       {small}*{getal1}={antwoord1} ')
print(f'pizzas small:      {medium}*{getal2}={antwoord2} ')
print(f'pizzas small:       {large}*{getal3}={antwoord3} ')
print('--------------------------------------------------')
print(f'te betalen:                      {total}')
