

prijs_per_vriend = 7.45
vip_5min = 0.37

aantal_personen = int(input('Met hoeveel mensen? '))
vip_aantal = int(input('Hoe vaak wilt u gebruik maken van VIP? '))


normaal_prijs = prijs_per_vriend * aantal_personen
vip_totaal = vip_5min * vip_aantal
totaal_prijs = normaal_prijs + vip_totaal


print(f'De prijs voor een dagje uit is {totaal_prijs} euro')
print(f'Dit geweldige dagje-uit met {aantal_personen} mensen in de Speelhal met {vip_aantal} VR kost je maar {totaal_prijs:.2f} euro')