aantal_lijstjes = int(input("Hoeveel lijstjes wil je genereren? "))

alle_lijstjes = []

for i in range(1, aantal_lijstjes + 1):
    lengte_lijstje = int(input(f"Hoe lang moet lijst {i} zijn? "))
    lijst = list(range(i, i * lengte_lijstje + 1, i))
    alle_lijstjes.append(lijst)

for index, lijst in enumerate(alle_lijstjes):
    print(f"Lijst {index}: {lijst}")