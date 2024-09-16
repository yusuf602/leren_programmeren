a = int(input('Kies een getal: '))
b = int(input('kies nog een getal: '))
max = a
min = a

if a > b:
    max = a
    print(f"a is het grootste getal: {max}")
elif b > a:
    min = a
    print(f"a is het kleinste getal: {min}")
else:
    a = b
    print(f'a is het kleinste getal')

print('Het minimum is: gevolgd door de waarde van Min')
print('Het maximum is: gevolgd door de waarde van Max')

        