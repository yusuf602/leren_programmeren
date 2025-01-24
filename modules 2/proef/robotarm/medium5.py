from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)
for i in range(4):
    robotArm.moveRight()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.grab()
for i in range(3):
    robotArm.moveRight()
robotArm.drop()
for i in range(4):
    robotArm.moveLeft()
robotArm.grab()
for i in range(5):
    robotArm.moveRight()
robotArm.drop()
for i in range(6):
    robotArm.moveLeft()
robotArm.grab()
for i in range(7):
    robotArm.moveRight()
robotArm.drop()
for i in range(8):
    robotArm.moveLeft()
robotArm.grab()
for i in range(9):
    robotArm.moveRight()
robotArm.drop()




