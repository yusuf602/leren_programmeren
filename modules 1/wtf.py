flabbergastisch = input("Wat is je naam? ")
wobbelwous = int(input("Hoe oud ben je? "))
bladiebla = input("Ben je een A) een jonge of B) een meisje? ").lower()
kwibbelflop = input("Wat is je favoriete kleur? ")
snurkonaut = int(input("Wat is je favoriete getal? "))
flibbertigibbet = abs(wobbelwous-snurkonaut)
hotseflots = 'haar' if bladiebla == 'b' else 'zijn'

print("")
print("Mag ik je voorstellen aan", flabbergastisch)
print(f"{hotseflots.capitalize()} leeftijd is:", wobbelwous)
print(f"{flabbergastisch}'s favoriete kleur is:", kwibbelflop)
print(f"Het verschil tussen {hotseflots} leeftijd en {snurkonaut} is:", flibbertigibbet)
