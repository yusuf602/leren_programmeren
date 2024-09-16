
a = int(input("Geef het eerste gehele getal: "))
b = int(input("Geef het tweede gehele getal: "))

if a > b:
    Max = a
    Min = b
    print(f"a is het grootste getal: {Max}")
elif b > a:
    Max = b
    Min = a
    print(f"a is het kleinste getal: {Min}")
else:
    Max = Min = a
    print("a en b zijn even groot")

print(f"Het minimum is: {Min}")
print(f"Het maximum is: {Max}")