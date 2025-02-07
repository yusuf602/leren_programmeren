import random
from fruitmand import fruitmand

aantal = int(input("kies een getal: "))

for i in range(aantal):
    print(random.choice(fruitmand))