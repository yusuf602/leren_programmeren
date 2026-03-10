import random

speciale_ballen = ["groen", "groen", "groen", "rood", "rood", "rood"]
ballen_team1 = [2,4,6,8,10]
ballen_team2 = [1,3,5,7,9]


ballenbak = speciale_ballen + ballen_team1 + ballen_team2

def grabbelen(ballenbak):
    bal1 = random.choice(ballenbak)
    ballenbak.remove(bal1)
    bal2 = None
    if bal1 != "rood":
        bal2 = random.choice(ballenbak)
        ballenbak.remove(bal2)
    return bal1, bal2