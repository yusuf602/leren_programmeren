import termcolor

def vraaggegeven():
    naam = input("Voer een naam in: ""geel")
    leeftijd = int(input('Voer een leeftijd in: '))
    woonplaats = input('Woonplaats in: ')
    return {'name': naam, 'age': leeftijd, 'city': woonplaats}

def doorvragen():
    lijst = []
    while True:
        gegevens = vraaggegeven()
        lijst.append(gegevens)
        vraag = input('Toets enter om door te gaan of "stop" om te printen: ').lower().strip()
        if vraag == 'stop':
            break
    return lijst