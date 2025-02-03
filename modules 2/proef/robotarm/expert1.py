from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[1],0)

robotArm.grab()
for i in range(5):
    robotArm.moveRight()

robotArm.drop()

for i in range(4):
    robotArm.moveLeft()

robotArm.grab()
for i in range(5):
    robotArm.moveRight()

robotArm.drop()
for i in range(5):
    robotArm.moveLeft()

robotArm.grab()
for i in range(5):
    robotArm.moveRight()

robotArm.drop()
for i in range(4):
    robotArm.moveLeft()

robotArm.grab()
for i in range(5):
    robotArm.moveRight()

robotArm.drop()
for i in range(2):
    for i in range(5):
        robotArm.moveLeft()

    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()

    robotArm.drop()

for i in range(4):
    robotArm.moveLeft()

robotArm.grab()
for i in range(5):
    robotArm.moveRight()

robotArm.drop()
for i in range(3):
    for i in range(5):
        robotArm.moveLeft()

    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()

    robotArm.drop()




