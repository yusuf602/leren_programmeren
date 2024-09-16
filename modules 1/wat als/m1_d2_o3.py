gasten = False
gastheer = False
chips = False
drank = False

conditie_1 = gasten or gastheer

conditie_2 = gastheer or (gasten and chips and drank)

conditie_3 = not (chips and not drank)

conditie_4 = not (gasten and not (chips or drank))

conditie_5 = not (gastheer and not drank)

conditie_6 = not (chips and not (gasten or gastheer or drank))

if conditie_1 and conditie_2 and conditie_3 and conditie_4 and conditie_5 and conditie_6:
    print("Het feest kan beginnen!")
else:
    print("No party")