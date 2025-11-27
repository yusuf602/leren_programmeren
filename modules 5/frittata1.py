from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = int(input()) # replace this with better input

# ----- CALCULATIONS ----
# calculate factor 
factor = nr_persons /RECIPE_PERSONS
eggs_amount = AMOUNT_EGGS * factor
milk_amount = AMOUNT_MILK * factor
salt_amount = AMOUNT_SALT * factor
pepper_amount = AMOUNT_PEPPER * factor
oil_amount = AMOUNT_OIL * factor
onion_amount = AMOUNT_ONIONS * factor
garlic_amount = AMOUNT_GARLICS * factor
paprika_amount = AMOUNT_PAPRIKAS * factor
spinach_amount = AMOUNT_SPINACH * factor
cheese_amount = AMOUNT_CHEESE * factor

print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
print(f'{eggs_amount} {UNIT_EGGS} {TXT_EGGS}')
print(f'{milk_amount} {UNIT_MILK} {TXT_MILK}')
print(f'{salt_amount} {UNIT_SALT} {TXT_SALT}')
print(f'{pepper_amount} {UNIT_PEPPER} {TXT_PEPPER}')
print(f'{oil_amount} {UNIT_OIL} {TXT_OIL}')
print(f'{onion_amount} {UNIT_ONIONS} {TXT_ONIONS}')
print(f'{garlic_amount} {UNIT_GARLICS} {TXT_GARLICS}')
print(f'{paprika_amount} {UNIT_PAPRIKAS} {TXT_PAPRIKAS}')
print(f'{spinach_amount} {UNIT_SPINACH} {TXT_SPINACH}')
print(f'{cheese_amount} {UNIT_CHEESE} {TXT_CHEESE}')
print('-----------------------------------------------')