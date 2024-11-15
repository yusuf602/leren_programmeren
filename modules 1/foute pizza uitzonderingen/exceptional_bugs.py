import random

#selecteer 2 nummers
num1 = random.randint(1,10)
num2 = random.randint(5,15)

#vraag om een antwoord
number = input('Weet jij wat '+str(num1)+'+'+str(num2)+' is? ') 

#geef reactie op het antwoord
try:
    if int(number) == num1 + num2:
        print('Dat is juist')
    else:
        print('Nee dat klopt niet')
except ValueError:
    print('Dat is geen nummer!')
