# Controleert of een getal een priemgetal is.
def is_prime(number:int) -> bool:
    # Getallen kleiner dan of gelijk aan 1 zijn geen priemgetallen
    if number <= 1:
        return False
    
    # als het nummer gelijk is aan 2 return zijn priemgetallen
    if number == 2:
        return True
    
    # Alle even getallen groter dan 2 zijn geen priemgetallen
    if number % 2 == 0:
        return False
    
    # ...
    max_divisor = int(number**0.5) + 1
    for d in range(3, max_divisor, 2):
        if number % d == 0:
            return False
    
    # ...
    return True