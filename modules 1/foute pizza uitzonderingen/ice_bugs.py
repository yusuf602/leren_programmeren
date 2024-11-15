def convertToEuroText(amount):
    return "€{:.2f}".format(float(amount)).replace(".", ",")

SMALL_PRICE = 1.25
MEDIUM_PRICE = 2.10

smal_amount = int(input('Hoeveel ijsjes van {} wil je bestellen? '.format(convertToEuroText(SMALL_PRICE))))
medium_amount = int(input('En hoeveel ijsjes van {} wil je bestellen? '.format(convertToEuroText(MEDIUM_PRICE))))

totalPrice = (smal_amount * SMALL_PRICE) + (medium_amount * MEDIUM_PRICE)

print('Dat is dan {} totaal'.format(convertToEuroText(totalPrice)))
