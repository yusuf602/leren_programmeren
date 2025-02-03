from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

for i in range(9):
    robotArm.grab() 

    color = robotArm.scan()  

    if color == "red":  
        steps_to_right = 9 - i  
        for _ in range(steps_to_right):
            robotArm.moveRight()

        robotArm.drop()  

        for _ in range(steps_to_right):
            robotArm.moveLeft()

    else:
        robotArm.drop()

    if i < 8:
        robotArm.moveRight()
