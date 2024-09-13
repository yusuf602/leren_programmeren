from termcolor import colored, cprint, COLORS

prijs_croissantjes = 0.39
aantal_croissanjes = int(input("hoeveel croissanten?"))

prijs_stokbrood = 2.78
aantal_stokbrood = int(input("hoeveel stokbrood?"))

korting_bon = 0.50
aantal_kortingsbonnen = int(input("hoeveel kortingsbonnen?"))

totaal_croissant = prijs_croissantjes * aantal_croissanjes
totaal_stokbrood = prijs_stokbrood * aantal_stokbrood

totaal_korting = korting_bon * aantal_kortingsbonnen

totaal_tebetalen = (totaal_croissant + totaal_stokbrood) - totaal_korting

print(f"De totale te betalen bedrag voor de feestlunch is {colored(totaal_tebetalen, 'red')} euro.")

print (f'De feestlunch kost je bij de bakker {totaal_tebetalen} euro voor de {totaal_croissant} croissantjes en de {totaal_stokbrood:.2f} stokbroden als de {totaal_korting} kortingsbonnen nog geldig zijn!')
