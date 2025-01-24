from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.beginner import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

robotArm.moveRight()
for i in range(6):
    robotArm.grab()
    if robotArm._color == 'g':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    elif robotArm._color == 'b':
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()

        
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()