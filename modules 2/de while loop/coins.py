# name of student 
# number of student
# purpose of program
# structure of program 
# and returns the maximum 

# Muntsoorten, uitgebreid met 1, 2 en 5 euro munten, omgezet naar centen
coinValues = [500, 200, 100, 50, 20, 10, 5, 2, 1]  # In centen

# Initialiseren van variabelen
toPay = int(float(input('Amount to pay (in euros): ')) * 100)  # Het te betalen bedrag in centen
paid = int(float(input('Paid amount (in euros): ')) * 100)  # Het betaalde bedrag in centen
change = paid - toPay  # Het te geven wisselgeld

# Lijst voor het aantal teruggegeven munten per type munt
coinsReturned = {coin: 0 for coin in coinValues}

# Controleer of het betaalde bedrag groter is dan het te betalen bedrag
if change < 0:
    print("The paid amount is less than the required amount. Please provide the correct amount.")
else:
    # Teruggeven van wisselgeld
    while change > 0 and len(coinValues) > 0:
        coinValue = coinValues.pop(0)  # Kies de grootste beschikbare munt
        nrCoins = change // coinValue  # Hoeveel muntstukken kunnen er van deze muntwaarde worden gegeven?

        if nrCoins > 0:
            # Print het maximale aantal munten dat teruggegeven kan worden
            print(f'Return maximal {nrCoins} coins of {coinValue} cents.')
            nrCoinsReturned = int(input(f'How many coins of {coinValue} cents did you return? '))

            # Voeg de munten toe aan de teruggegeven lijst
            coinsReturned[coinValue] += nrCoinsReturned
            change -= nrCoinsReturned * coinValue  # Trek het aantal gegeven munten van het wisselgeld af

    # Controleer of het wisselgeld volledig is teruggegeven
    if change > 0:
        print(f'Change not returned: {change} cents.')
    else:
        print('Change returned successfully.')

    # Toon het overzicht van alle teruggegeven munten
    print("\nOverview of returned coins:")
    for coin in coinValues:
        if coinsReturned[coin] > 0:
            print(f'{coinsReturned[coin]} coins of {coin} cents')

    if change > 0:
        print("Note: Not all the required change could be returned.")
    else:
        print("All required change has been returned.")
