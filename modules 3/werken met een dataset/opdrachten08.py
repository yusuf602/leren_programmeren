import fruitmand

watermeloen = {
    "name": "watermeloen",
    "color": "groen",
    "weight": 1500,
    "round": True
}
fruitmand.fruitmand.append(watermeloen)

totaal_gewicht = sum(fruit["weight"] for fruit in fruitmand.fruitmand)
print(f"{totaal_gewicht}")