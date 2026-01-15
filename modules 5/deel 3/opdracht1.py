
prijzen = {
    "small" : 6.50,
    "medium" : 9.30,
    "large": 11.10
}

def vraag_aantal_pizzas(pizza_type):
    while True:
        try:
            aantal = int(input(f'Hoeveel {pizza_type} pizzas wil je bestellen? '))
            if aantal < 0:
                print("Voer een positief getal in (0 of hoger).")
            else:
                return aantal
        except  ValueError:
                print("Voer een geldig geheel getal in (bijv. 0, 1, 2...)") 


aantallen = {}
for pizza_type in prijzen:
    aantallen[pizza_type] = vraag_aantal_pizzas(pizza_type)


totaal = 0
print('******************** KASSA BON ********************')
for pizza_type in prijzen:
    prijs = prijzen[pizza_type]
    aantal = aantallen[pizza_type]
    subtotaal = prijs * aantal
    totaal += subtotaal
    print(f'{pizza_type.capitalize():<10}: {prijs:.2f} * {aantal} = {subtotaal:.2f}')

print('--------------------------------------------------')
print(f'Te betalen: {totaal:.2f}')