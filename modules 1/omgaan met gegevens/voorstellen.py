naam = input("Wat is je naam? ")
leeftijd = int(input("Hoe oud ben je? "))
geslacht = input("Ben je een A) een jonge of B) een meisje? ").lower()
kleur = input("Wat is je favoriete kleur? ")
getal = int(input("Wat is je favoriete getal? "))
verschil_leeftijd = abs(leeftijd-getal)
geslacht2 = 'haar' if geslacht == 'b' else 'zijn'


print("Mag ik je voorstellen aan", naam)
print(f"{geslacht2.capitalize()} leeftijd is:", leeftijd)
print(f"{naam}'s favoriete kleur is:", kleur)
print(f"Het verschil tussen {geslacht2} leeftijd en {getal} is:", verschil_leeftijd)