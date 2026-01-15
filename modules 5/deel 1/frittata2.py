from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')

# -------- INPUT --------
nr_persons = int(input("Met hoeveel personen komen jullie eten? "))

# ----- CALCULATIONS ----
factor = nr_persons / RECIPE_PERSONS

# Hulpfunctie om volume correct af te ronden
def format_ml(value: float) -> str:
    if value < 100:
        return f"{value:.1f} ml"
    else:
        return f"{value:.0f} ml"

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

# Print alle ingrediënten
for amount, unit, name in ingredients:
    new_amount = amount * factor

    amount_str = str_amount_fraction(new_amount)
    unit_str   = str_units(new_amount, unit)
    name_str   = str_single_plural(new_amount, name)

    ml_info = ""

    # Alleen lepels, theelepels, kopjes krijgen ml
    if unit in (UNIT_SPOONS, UNIT_TEASPOONS, UNIT_CUPS):
        amount_ml = unit2ml(new_amount, unit)
        ml_info = f" ({format_ml(amount_ml)})"

    print(f"{amount_str} {unit_str} {name_str}{ml_info}")

print('-----------------------------------------------')
