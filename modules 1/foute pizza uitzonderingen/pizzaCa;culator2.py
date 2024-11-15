#voornaam, achternaam en opdracht: Pizza calculator
small = 6.5
medium = 9.30
large = 11.10

def vraag_aantal_pizzas(pizza_type):
    while True:
        try:
            aantal = int(input(f'hoeveel {pizza_type} wil je bestellen? '))
            if aantal < 0:
                print('voer asltublieft een positief getal in. ')
            else:
                return aantal
        except ValueError:
             print('voer alstublieft een geldig aantal in. ')

getal1 = vraag_aantal_pizzas('small')
getal2 = vraag_aantal_pizzas('medium')
getal3 =vraag_aantal_pizzas('large')

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