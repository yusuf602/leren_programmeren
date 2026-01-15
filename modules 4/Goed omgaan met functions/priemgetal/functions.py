def is_prime(number: int) -> bool:
    """Controleert of een getal een priemgetal is."""
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    max_divisor = int(number**0.5) + 1
    for d in range(3, max_divisor, 2):
        if number % d == 0:
            return False
    return True

def priem_tot_en_met(n) -> list:
    """Geeft een lijst van alle priemgetallen tot en met n."""
    list=[]
    for i in range (n+1):
        if is_prime(i): 
            list.append(i)
    return list
def first_n_primes(n) -> list:
    """Geeft een lijst van de eerste n priemgetallen."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def primes_between(start, end) -> list:
    """Geeft een lijst van priemgetallen tussen start en end (inclusief grenzen)."""
    return [num for num in range(start, end + 1) if is_prime(num)]


def run_tests():
    print(f"Priemgetallen tot en met 10: {priem_tot_en_met(10)}")
    print(f"Priemgetallen tot en met 20: {priem_tot_en_met(20)}")  

    print(f"Eerste 5 priemgetallen: {first_n_primes(5)}") 
    print(f"Eerste 10 priemgetallen: {first_n_primes(10)}")  

    print(f"Priemgetallen tussen 10 en 30: {primes_between(10, 30)}")  
    print(f"Priemgetallen tussen 50 en 60: {primes_between(50, 60)}")  

run_tests()
