lst_id = [str(i) for i in input().split()]



def score(id):
    sco = 0
    LastThree = int(id[-3])*100 + int(id[-2])*10 + int(id[-1])
    if id[3:6] == '902':
        sco += 2000
    if id[3:6] == '901':
        sco += 1000
    if id[1:3] == '04':
        sco += 100
    if LastThree % 3 == 0 or LastThree % 5 == 0 or LastThree % 7 == 0:
        sco += 10
    return sco

lst_id.sort(key=score, reverse=True)

for i in lst_id:
    print(i)

