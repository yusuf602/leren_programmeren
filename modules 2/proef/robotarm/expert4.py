from RobotArm import RobotArm
# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:
def moveamountLeft(nummer):
    for x in range(nummer):
        robotArm.moveLeft()
def moveamountRight(nummer):
    for x in range(nummer):
        robotArm.moveRight()

robotArm.grab()
robotArm.scan()
print(robotArm._color)
if robotArm._color == "r":
    moveamountRight(7)
    robotArm.drop()
    moveamountLeft(6)
elif robotArm._color == "g":
    moveamountRight(8)
    robotArm.drop()
    moveamountLeft(7)
else:
    moveamountRight(9)
    robotArm.drop()
    moveamountLeft(8)
robotArm.grab()
if robotArm._color == "r":
    moveamountRight(6)
    robotArm.drop()
    moveamountLeft(5)
elif robotArm._color == "g":
    moveamountRight(7)
    robotArm.drop()
    moveamountLeft(6)
else:
    moveamountRight(8)
    robotArm.drop()
    moveamountLeft(7)
robotArm.grab()
if robotArm._color == "r":
    moveamountRight(5)
    robotArm.drop()
    moveamountLeft(4)
elif robotArm._color == "g":
    moveamountRight(6)
    robotArm.drop()
    moveamountLeft(5)
else:
    moveamountRight(7)
    robotArm.drop()
    moveamountLeft(6)
robotArm.grab()
if robotArm._color == "r":
    moveamountRight(4)
    robotArm.drop()
    moveamountLeft(3)
elif robotArm._color == "g":
    moveamountRight(5)
    robotArm.drop()
    moveamountLeft(4)
else:
    moveamountRight(6)
    robotArm.drop()
    moveamountLeft(5)
robotArm.grab()
if robotArm._color == "r":
    moveamountRight(3)
    robotArm.drop()
    moveamountLeft(2)
elif robotArm._color == "g":
    moveamountRight(4)
    robotArm.drop()
    moveamountLeft(3)
else:
    moveamountRight(5)
    robotArm.drop()
    moveamountLeft(4)
robotArm.grab()
if robotArm._color == "r":
    moveamountRight(2)
    robotArm.drop()
elif robotArm._color == "g":
    moveamountRight(3)
    robotArm.drop()
else:
    moveamountRight(4)
    robotArm.drop()
# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

