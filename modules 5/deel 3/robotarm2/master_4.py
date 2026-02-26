from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from master import *

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:


order = []
for i in range(4):
    robotArm.grab()
    block = robotArm.scan()
    position = 1
    order.append(block)
    position += 1
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
print(order)
for i in range(4):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()

next_block = 4



to_move = 9
to_end = 8
order_spot = 3
unsafe_index = [0]
for i in range(to_move):robotArm.moveRight()

successful_grabs = 0
while successful_grabs < 4:
    #robotArm.moveRight()
    to_move -= 1
    x = robotArm.stackIndex()

    if x not in unsafe_index:
        robotArm.grab()
        block = robotArm.scan()
    else:
        print("")

    if block != order[order_spot]:
        
        robotArm.drop()
        robotArm.moveLeft()

    else:
        #robotArm.grab()
        block = robotArm.scan()
        unsafe_index.append(robotArm.stackIndex())
        order_spot -= 1
        ind = robotArm.stackIndex()

        for i in range(ind - 1):
            robotArm.moveLeft()
        robotArm.drop()

        for i in range(to_end):robotArm.moveRight()
        print(to_move)
        successful_grabs += 1
        print("successful grabs:", successful_grabs)
    print(unsafe_index)
# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

