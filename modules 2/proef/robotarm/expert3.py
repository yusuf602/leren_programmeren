from RobotArm import RobotArm
from challenges.expert import challenges

# Laad de robotarm met een uitdaging
robotArm = RobotArm(challenges[3], 0)

# Beginpositie van de stapel
start_positie = 1
huidige_positie = start_positie
drop_positie = start_positie + 1  # Begin met droppen bij positie 2

# Verplaats alle blokken totdat de stapel leeg is
while True:
    robotArm.grab()  # Pak een blok
    if not robotArm.scan():  # Als er geen blok is, stop de loop
        break

    # Ga naar de volgende drop-positie en laat het blok vallen
    for _ in range(drop_positie - huidige_positie):
        robotArm.moveRight()

    robotArm.drop()  # Laat het blok vallen

    # Keer terug naar de stapelpositie
    for _ in range(drop_positie - huidige_positie):
        robotArm.moveLeft()

    # Update de drop-positie voor het volgende blok
    drop_positie += 1  

# Stop de simulatie
robotArm.wait()

  