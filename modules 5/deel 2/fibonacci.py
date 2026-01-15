#fibonnaci reeks

lijst =  [0,1]
loop_range= 1000



for i in range (loop_range):
       nieuw = lijst[i] + lijst[i + 1]
       lijst.append(nieuw)

print(lijst)