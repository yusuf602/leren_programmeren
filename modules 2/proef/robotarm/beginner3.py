from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.beginner import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)
for i in range(5):
    robotArm.grab()

    for i in range(4):
        robotArm.moveRight()


    robotArm.drop()
    for i in range(4):
        robotArm.moveLeft()

robotArm.report()

# want help? Unlock code below!
robotArm.help()


