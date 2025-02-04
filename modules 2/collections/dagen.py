week = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

print("Alle dagen van de week:")
for dag in week:
    print(f'- {dag}')
print('')

print("De doordeweekse dagen zijn:")
print(" - ".join(week[:5]))  
print('')

print("De weekenddagen zijn:")
print(" - ".join(week[5:]))  
print('')

print("Alle dagen van de week in omgekeerde volgorde:")
print(" <-- ".join(reversed(week)))
print('')

print("De doordeweekse dagen in omgekeerde volgorde:")
print(" - ".join(reversed(week[:5])))
print('')

print("De weekenddagen in omgekeerde volgorde:")
print(" - ".join(reversed(week[5:])))
print('')
