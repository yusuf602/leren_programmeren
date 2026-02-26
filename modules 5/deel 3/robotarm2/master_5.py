from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from master import *

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:

color_list = {}

for i in range(10):
    robotArm.grab()
    posititie = robotArm.stackIndex()
    current_color = robotArm.scan()

    if current_color not in color_list:
        
        color_list[current_color] = posititie
        robotArm.drop()
        if i < 9:
            robotArm.moveRight()
    
    else:
        dubble_color_position = color_list[current_color]
        while robotArm.stackIndex() != dubble_color_position:
            robotArm.moveLeft()
        

        robotArm.drop()
        break
print(color_list)

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

