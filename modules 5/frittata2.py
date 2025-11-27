from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')

# -------- INPUT --------
nr_persons = int(input("Met hoeveel personen komen jullie eten? "))

# ----- CALCULATIONS ----
factor = nr_persons / RECIPE_PERSONS

# Ingrediëntenlijst
ingredients = [
    (AMOUNT_EGGS, UNIT_EGGS, TXT_EGGS),
    (AMOUNT_MILK, UNIT_MILK, TXT_MILK),
    (AMOUNT_SALT, UNIT_SALT, TXT_SALT),
    (AMOUNT_PEPPER, UNIT_PEPPER, TXT_PEPPER),
    (AMOUNT_OIL, UNIT_OIL, TXT_OIL),
    (AMOUNT_ONIONS, UNIT_ONIONS, TXT_ONIONS),
    (AMOUNT_GARLICS, UNIT_GARLICS, TXT_GARLICS),
    (AMOUNT_PAPRIKAS, UNIT_PAPRIKAS, TXT_PAPRIKAS),
    (AMOUNT_SPINACH, UNIT_SPINACH, TXT_SPINACH),
    (AMOUNT_CHEESE, UNIT_CHEESE, TXT_CHEESE),
]

print('-----------------------------------------------')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')

for amount, unit, name in ingredients:
    new_amount = amount * factor

    amount_str = str_amount_fraction(new_amount)  # bijv. "3¼", "1½", "¾"
    unit_str   = str_units(new_amount, unit)      # bijv. "kopjes", "lepel"
    name_str   = str_single_plural(new_amount, name)  # bijv. "groot ei", "grote eieren"

    # ----- Print netjes -----
    print(f"{amount_str} {unit_str} {name_str}")

print('-----------------------------------------------')
