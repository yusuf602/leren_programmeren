from variabelen2 import doorvragen
import termcolor

gegevens = doorvragen()
for i in range(len(gegevens)):
    print(f"{gegevens[i]['name']} die in {gegevens[i]['city']} woont, is {gegevens[i]['age']} jaar.")


