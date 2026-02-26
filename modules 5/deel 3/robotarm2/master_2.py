from RobotArm import RobotArm
from master import *

robotArm = RobotArm(challenges[2], 0)

kleuren = []
for i in range(4):
    robotArm.moveRight()
for i in range(5):
    robotArm.grab()
    kleur = robotArm.scan()
    kleuren.append(kleur)
    robotArm.drop()
    robotArm.moveRight()
robotArm.grab()
kleur = robotArm.scan()
kleuren.append(kleur)
robotArm.drop()

kleur1 = kleuren[0]
kleur2 = None
kleur3 = None

aantal1 = 0
aantal2 = 0
aantal3 = 0

for kleur in kleuren:
    if kleur == kleur1:
        aantal1 += 1
    elif kleur2 is None:
        kleur2 = kleur
        aantal2 += 1
    elif kleur == kleur2:
        aantal2 += 1
    else:
        kleur3 = kleur
        aantal3 += 1


if aantal1 == 3:
    eerst = kleur1
elif aantal2 == 3:
    eerst = kleur2
else:
    eerst = kleur3

if aantal1 == 2:
    tweede = kleur1
elif aantal2 == 2:
    tweede = kleur2
else:
    tweede = kleur3

if aantal1 == 1:
    derde = kleur1
elif aantal2 == 1:
    derde = kleur2
else:
    derde = kleur3


for i in range(5):
    robotArm.moveLeft()


stapel_vakken = {
    eerst: 1,   
    tweede: 2,  
    derde: 3    
}

positie_arm = 1

stapel_vakken = {
    eerst: 1,   
    tweede: 2, 
    derde: 3    
}

def ga_naar(vak):
    global positie_arm
    while positie_arm < vak:
        robotArm.moveRight()
        positie_arm += 1
    while positie_arm > vak:
        robotArm.moveLeft()
        positie_arm -= 1

def stapel_blokken(kleur, aantal):
    global positie_arm
    gevonden = 0
    for i in range(10, 0, -1):
        ga_naar(i)        
        robotArm.grab()
        if robotArm.scan() == kleur:
            ga_naar(stapel_vakken[kleur])
            robotArm.drop()
            gevonden += 1
            if gevonden == aantal:
                break
        else:
            robotArm.drop()

stapel_blokken(eerst, 3)
stapel_blokken(tweede, 2)
stapel_blokken(derde, 1)



volgende_vak = 1 


positie_arm = 1

blokken_vakjes = kleuren  # kleuren = lijst van kleuren van vak 5 t/m 10

# Functie om blokken van een bepaalde kleur te stapelen


# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

