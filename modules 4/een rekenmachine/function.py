def addition(number1: float, number2: float) -> float:
    """Voegt twee getallen bij elkaar."""
    return number1 + number2

def subtraction(number1: float, number2: float) -> float:
    """Trekt het tweede getal af van het eerste getal."""
    return number1 - number2

def multiplication(number1: float, number2: float) -> float:
    """Vermenigvuldigt twee getallen."""
    return number1 * number2

def division(number1: float, number2: float) -> float:
    """Deelt het eerste getal door het tweede getal."""
    if number2 == 0:
        return "Fout: Delen door nul is niet toegestaan."
    return number1 / number2
