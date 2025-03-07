from fruitmand import fruitmand

langste_fruit = max(fruitmand, key=lambda fruit: len(fruit["name"]))

print(f"Het fruit met de langste naam is een {langste_fruit['name']}.")
print(f'lengte:{len(langste_fruit['name'])}')
print(f"Kleur: {langste_fruit['color']}")
print(f"Gewicht: {langste_fruit['weight']} gram")