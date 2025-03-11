from variabelen2 import doorvragen
import termcolor

gegevens = doorvragen()
for i in range(len(gegevens)):
    print(f"{termcolor.colored(gegevens[i]['name'],'green')} die in {termcolor.colored(gegevens[i]['city'],'yellow')} woont, is {termcolor.colored(gegevens[i]['age'],'red')} jaar.")


