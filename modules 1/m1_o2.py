from termcolor import colored, cprint, COLORS
prijs_per_vriend = 7.45
aantal_personen = 4

normaal_prijs = prijs_per_vriend * aantal_personen

vip_5min = 0.37
vip_min = 9

vip_totaal = vip_5min * vip_min

totaal_prijs = normaal_prijs * vip_totaal

cprint(f'de prijs voor een dagje uit is {colored(totaal_prijs,'red')} euro')

print(f'Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar {totaal_prijs:.2f} euro')