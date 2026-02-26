from RobotArm import RobotArm
from master import *

# Laad het level
robotArm = RobotArm(challenges[3], 0)

# Posities (0-indexed)
doel_rijen = [0, 1, 8, 9]  # Doelrijen 1,2,9,10
start_rijen = [3, 4, 5, 6] # Start rijen 4 t/m 7

positie = 0
kleur_naar_rij = {}

# Functie om naar een rij te bewegen
def ga_naar(doel):
    global positie
    while positie < doel:
        robotArm.moveRight()
        positie += 1
    while positie > doel:
        robotArm.moveLeft()
        positie -= 1

# Omdat elke start rij exact 4 blokken heeft
for ronde in range(4):  # 4 blokken per rij
    for rij in start_rijen:
        ga_naar(rij)  # Ga naar start rij
        robotArm.grab()          # Pak bovenste blok
        kleur = robotArm.scan()  # Scan kleur

        # Wijs doelrij toe als nieuw
        if kleur not in kleur_naar_rij:
            for r in doel_rijen:
                if r not in kleur_naar_rij.values():
                    kleur_naar_rij[kleur] = r
                    break

        # Ga naar doelrij en drop
        ga_naar(kleur_naar_rij[kleur])
        robotArm.drop()
        # Terug naar start rij
        ga_naar(rij)

# Eindrapport
robotArm.report()
