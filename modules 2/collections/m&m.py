import random

kleur = ("oranje", "blauw", "groen", "bruin")

hoeveel= int(input("hoeveel M&M's moet er in een zak? "))

mylist= []

for i in range(hoeveel):
    mylist.append(random.choice(kleur))

print(mylist)