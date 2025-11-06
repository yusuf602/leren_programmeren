def is_prime(number: int) -> bool:
    """Controleert of een getal een priemgetal is."""
#als het gelijk en of kleiner is dan 1 is het geen  prime getal
    if number <= 1:
        return False
#als het gelijk is aan 2 is het wel een prime getal
    if number == 2:
        return True
#als het gelijk deel baar is door 2 gelijk is aan 0 is het geen prime getal
    if number % 2 == 0:
        return False

    max_divisor = int(number**0.5) + 1
    for d in range(3, max_divisor, 2):
        if number % d == 0:
            return False
    return True

# 1. Alle priemgetallen tot en met een bepaald getal
def priem_tot_en_met(n: int) -> list:
    """Geeft een lijst van alle priemgetallen tot en met n."""
    list=[]
    for i in range (n+1):
        if is_prime(i): 
            list.append(i)
    return list
# 2. De eerste N priemgetallen
def first_n_primes(n: int) -> list:
    """Geeft een lijst van de eerste n priemgetallen."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# 3. Priemgetallen tussen twee getallen
def primes_between(start: int, end: int) -> list:
    """Geeft een lijst van priemgetallen tussen start en end (inclusief grenzen)."""
    return [num for num in range(start, end + 1) if is_prime(num)]

# ✅ HOOFDPROGRAMMA

# Functie-aanroepen (gebruiker hoeft geen input te geven, alles gebeurt via parameters)
def run_tests():
    # Test voor priem_tot_en_met()
    print(f"Priemgetallen tot en met 10: {priem_tot_en_met(10)}")  # [2, 3, 5, 7]
    print(f"Priemgetallen tot en met 20: {priem_tot_en_met(20)}")  # [2, 3, 5, 7, 11, 13, 17, 19]

    # Test voor first_n_primes()
    print(f"Eerste 5 priemgetallen: {first_n_primes(5)}")  # [2, 3, 5, 7, 11]
    print(f"Eerste 10 priemgetallen: {first_n_primes(10)}")  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # Test voor primes_between()
    print(f"Priemgetallen tussen 10 en 30: {primes_between(10, 30)}")  # [11, 13, 17, 19, 23, 29]
    print(f"Priemgetallen tussen 50 en 60: {primes_between(50, 60)}")  # [53, 59]

# Functies aanroepen zonder input
run_tests()
