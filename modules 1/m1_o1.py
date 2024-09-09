prijs_croissantjes = 0.39
aantal_croissanjes = 17

prijs_stokbrood = 2.78
aantal_stokbrood = 2

korting_bon = 0.50
aantal_kortingsbonnen = 3 

totaal_croissant = prijs_croissantjes * aantal_croissanjes
totaal_stokbrood = prijs_stokbrood * aantal_stokbrood

totaal_korting = korting_bon * aantal_kortingsbonnen

totaal_tebetalen = (totaal_croissant + totaal_stokbrood) - totaal_korting

print(f"De totale te betalen bedrag voor de feestlunch is {totaal_tebetalen} euro.")

print (f'De feestlunch kost je bij de bakker {totaal_tebetalen} euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!')
