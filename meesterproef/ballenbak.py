import random

ROOD = "rood"
GROEN = "groen"

BALLEN_TEAM_1 = [2, 4, 6, 8, 10]
BALLEN_TEAM_2 = [1, 3, 5, 7, 9]


def maak_ballenbak():
    speciale_ballen = [GROEN, GROEN, GROEN, ROOD, ROOD, ROOD]
    return speciale_ballen + BALLEN_TEAM_1 + BALLEN_TEAM_2


def grabbelen(ballenbak):
    if len(ballenbak) == 0:
        return None, None

    bal1 = random.choice(ballenbak)
    ballenbak.remove(bal1)

    if bal1 == ROOD or len(ballenbak) == 0:
        return bal1, None

    bal2 = random.choice(ballenbak)
    ballenbak.remove(bal2)

    return bal1, bal2


def tel_speciale_ballen(ballen):
    rode_ballen = 0
    groene_ballen = 0

    for bal in ballen:
        if bal == ROOD:
            rode_ballen += 1
        elif bal == GROEN:
            groene_ballen += 1

    return rode_ballen, groene_ballen


if __name__ == "__main__":
    ballenbak = maak_ballenbak()
    bal1 = random.choice(ballenbak)
    print("Voorbeeldbal:", bal1)