from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.basic import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)
robotArm.grab()
for i in range(9):
    robotArm.moveRight()
robotArm.drop()

for i in range(5):
  robotArm.moveLeft()

robotArm.grab()
for i in range(5):
    robotArm.moveRight()

robotArm.drop()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.moveRight()
robotArm.drop()
