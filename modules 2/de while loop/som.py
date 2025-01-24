list = []
limiet = 1000
begin = 50
totaal = 0
while totaal <= limiet:
    totaal = totaal + begin
    list.append(begin)
    for i in range(len(list)):
        if i+1 == len(list):
            print(list[i], end="")
        else: 
            print(list[i], end=" + ")

    print(f' = {totaal}')
    begin = begin + 1



