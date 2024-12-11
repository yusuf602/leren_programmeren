from test_lib import *

month_discount_brands = 'Vespa,Kymco,Yamama'

MONTH_DISCOUNT_PERC = 10

def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:

    if price < 0: 
        return 'Prijs mag niet negatief zijn!'
    
    # Check if the brand is eligible for a discount
    eligible_brands = month_discount_brands.upper().split(',')
    if brand.upper() in eligible_brands:
        discount = (price * MONTH_DISCOUNT_PERC) / 100
    else:
        discount = 0

    return round(discount, 2)

scooter = [
    (100, "vespa"),
    (200, "kymco"),
    (300, "Yamama"),
]

for price, brand in scooter:
    discount = calc_discount(price, brand, month_discount_brands)
    test(
        f"test met prijs: {price}, merk: {brand}, korting: {discount}",
        price - discount,
        price - calc_discount(price, brand, month_discount_brands),
    )

report()
