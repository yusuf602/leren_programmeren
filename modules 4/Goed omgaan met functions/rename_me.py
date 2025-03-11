def is_even(getal: int) -> bool:
    """Controleert of een getal even is."""
    return getal % 2 == 0


def omgekeerde_woorden(zin: str) -> str:
    """Keert de volgorde van woorden in een zin om."""
    woorden = zin.split()
    omgekeerde_woorden = woorden[::-1]
    omgekeerde_zin = ' '.join(omgekeerde_woorden)
    return omgekeerde_zin


def unieke_karakters_aantal(tekst: str) -> int:
    """Berekent het aantal unieke karakters in een string."""
    unieke_karakters = set(tekst)
    return len(unieke_karakters)


def gemiddelde_woordlengte(zin: str) -> float:
    """Berekent de gemiddelde woordlengte in een zin."""
    woorden = zin.split()
    totale_lengte = sum(len(woord) for woord in woorden)
    return totale_lengte / len(woorden) if woorden else 0


def vermenigvuldigingstafel(getal: int, limiet: int = 10) -> None:
    """Print de vermenigvuldigingstafel van een getal tot een bepaalde limiet."""
    for i in range(1, limiet + 1):
        resultaat = i * getal
        print(f'{i} x {getal} = {resultaat}')



print(is_even(43)) 
print(omgekeerde_woorden("je vader")) 
print(unieke_karakters_aantal("banana"))
print(gemiddelde_woordlengte("Dit is een test")) 
vermenigvuldigingstafel(5)  