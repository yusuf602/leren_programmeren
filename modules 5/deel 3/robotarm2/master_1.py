from RobotArm import RobotArm
from master import *

robotArm = RobotArm(challenges[1], 0)

kleuren = []
aantal_blokken = 9   # op jouw screenshot staan er 9

# FASE 1: alles scannen
for i in range(aantal_blokken):
    robotArm.grab()
    kleur = robotArm.scan()
    kleuren.append(kleur)
    robotArm.drop()
    robotArm.moveRight()

# aparte kleur vinden
for kleur in kleuren:
    if kleuren.count(kleur) == 1:
        aparte_kleur = kleur
        break

# terug naar het begin
for i in range(aantal_blokken):
    robotArm.moveLeft()

# FASE 2: aparte kleur pakken
for i in range(aantal_blokken):
    robotArm.grab()
    if robotArm.scan() == aparte_kleur:
        break
    robotArm.drop()
    robotArm.moveRight()

robotArm.report()
robotArm.help()
