from test_lib import test, report

def get_value(data: str, separator: str, position: int) -> str:

    if not data: 
        return None

    if separator not in data:  
        if position == 0:
            return data
        return None

    splitted_strings = data.split(separator)

    if 0 <= position < len(splitted_strings): 
        return splitted_strings[position]

    return None  

toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'

test("Geldige positie (Positie 8, Bram:6)", "Bram:6", get_value(toets_data, ',', 8))
test("Eerste positie (Positie 0, Sofie:8)", "Sofie:8", get_value(toets_data, ',', 0))
test("Laatste positie (Positie 9, Maria:7)", "Maria:7", get_value(toets_data, ',', 9))
test("Negatieve positie (Positie -1, ongeldig)", None, get_value(toets_data, ',', -1))
test("Positie buiten bereik (Positie 10, ongeldig)", None, get_value(toets_data, ',', 10))

custom_data = 'appel|banaan|kers'
test("Aangepaste separator '|', Positie 1", "banaan", get_value(custom_data, '|', 1))

test("Lege datastring", None, get_value("", ',', 0))
test("Geen separator in data, geldige positie", "cat bird dog", get_value("cat bird dog", ',', 0))
test("Geen separator in data, ongeldige positie", None, get_value("cat bird dog", ',', 1))
test("Enkel element, geldige positie", "hond", get_value("hond", ',', 0))
test("Enkel element, ongeldige positie", None, get_value("hond", ',', 1))

report()

