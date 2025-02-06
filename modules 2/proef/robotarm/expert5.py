from RobotArm import RobotArm
# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:
def moveamountLeft(nummer):
    for x in range(nummer):
        robotArm.moveLeft()
def moveamountRight(nummer):
    for x in range(nummer):
        robotArm.moveRight()
position = 0
redcount = 0
yellowcount = 0
bluecount = 0

while True:
    robotArm.moveRight()
    position += 1
    robotArm.grab()
    robotArm.scan()
    print (robotArm._color)
    if position == 9:
        break
    if robotArm._color == "r":
        redcount +=1
        print(position)
    elif robotArm._color == "y":
        yellowcount +=1
        print(position)
    elif robotArm._color == "b":
        bluecount +=1
        print(position)
    robotArm.drop()

print(f"red = {redcount}, yellow = {yellowcount}, blue = {bluecount}")
robotArm.drop()
while True:
    if yellowcount > bluecount and yellowcount > redcount:
        mostcolor = "yellow"
        robotArm.grab()
        if robotArm._color != "y":
            robotArm.drop()
            robotArm.moveLeft()
        elif robotArm._color == "y":
            moveamountLeft(9)
            robotArm.drop()
            moveamountRight(9)
    elif bluecount > yellowcount and bluecount > redcount:
        mostcolor = "blue"
        robotArm.grab()
        if robotArm._color != "b":
            robotArm.drop()
            robotArm.moveLeft()
        elif robotArm._color == "b":
            moveamountLeft(9)
            robotArm.drop()
            moveamountRight(9)
        elif bluecount == redcount or bluecount == yellowcount or yellowcount == redcount:
            robotArm.grab()
            if robotArm._color in ["b", "r", "y"]:
                robotArm.drop()
                robotArm.moveLeft()
            else:
                moveamountLeft(9)
                robotArm.drop()
                moveamountRight(9)


    else:
        mostcolor = "red"
        robotArm.grab()
        if robotArm._color != "r":
            robotArm.drop()
            robotArm.moveLeft()
        elif robotArm._color == "r":
            moveamountLeft(9)
            robotArm.drop()
            moveamountRight(9)
            


# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
robotArm.showSolution()
# robotArm.wait()

