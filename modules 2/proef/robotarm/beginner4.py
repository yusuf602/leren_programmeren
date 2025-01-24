from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.beginner import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)
robotArm.moveRight()

for i in range(6):
    robotArm.grab()
    if robotArm._color == 'r':
     robotArm.moveRight()
     robotArm.drop()
     robotArm.moveLeft()
    elif robotArm._color == 'w':
     robotArm.moveLeft()
     robotArm.drop()
     robotArm.moveRight()


