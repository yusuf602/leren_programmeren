from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.basic import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)
 
robotArm.moveRight()
robotArm.grab()
if robotArm._color == "r":
    robotArm.moveLeft()
    robotArm.drop()
else:
    robotArm.moveRight()
    robotArm.drop()
    
