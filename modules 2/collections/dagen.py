#dagen van de week
week = ("maandag", "dinsdag", "woensdag", "dondernderdag", "vrijdag", "zaterdag", "zondag")  
weekend = ('zaterdagn', 'zondag')
doordeweek= ('maandag', 'dinsdag', 'woensdag', 'donderadag', 'vrijdaag')
#split de string in dagen

for dag in week:
 print(f'-{dag}')
print('')

print('alle dagen van de week')
print('')

#bepaalt de weekenddagen
print(f'{weekend}')
print('')
#bepaalt de dagen die een doordeweek zijn
doordeweekse_dagen = " - ".join(week[:5])

print("De doordeweekse dagen zijn:")
print(doordeweekse_dagen)
print('')

#bepaalt de dagen die een weekenddag zijn, maar in omgekeerde volgorde
dagenn = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

print("Alle dagen van de week in omgekeerde volgorde:")
print(" <-- ".join(reversed(dagenn)))

print('')

print("De werk dagen zijn:")
for dag in reversed(week[:5]):  # Pak de eerste 5 dagen (maandag t/m vrijdag)
    print('-' + dag)
print('')


print("De weekenddagen, achterstevoren, zijn:")

words = ' + '.join(reversed(weekend))
print (words)