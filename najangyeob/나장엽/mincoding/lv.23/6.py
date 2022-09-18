card = input()
cards = [0]*5
for i in range(len(card)):  
    cards[i] = int(card[i])




path = ['']*4
cnt = 0
def abc(level):
    if level == 4:
        global cnt
        cnt += 1
        return

    for i in range(5):
        if level>0 and abs(path[level-1] - cards[i]) > 3:
            continue
        path[level] = cards[i]
        abc(level+1)
        path[level] = ''

abc(0)
print(cnt)