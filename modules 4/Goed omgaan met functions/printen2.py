from variabelen import doorvragen
import termcolor

gegevens = doorvragen()
for persoon in gegevens:
    naam = termcolor.colored(persoon['name'], 'green')
    stad = termcolor.colored(persoon['city'], 'yellow')
    leeftijd = int(persoon['age'])
    
    berekende_leeftijd = leeftijd - 18

    if berekende_leeftijd >= 0:
        status = f"{berekende_leeftijd} jaar"
    else:
        status = f"nog niet"

    leeftijd_kleur = termcolor.colored(status, 'red')
    
    print(f"{naam} die in {stad} woont, die {leeftijd_kleur} volwassen is.")
