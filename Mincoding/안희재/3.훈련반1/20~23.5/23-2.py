# 모두 다른 -> 중복x => "순열"
word = input()
cards = [word[0], word[1], word[2], word[3]]
path = [''] * 4
cnt = 0

def abc(level):
    if level == 4:
        global cnt
        cnt += 1
        return
    
    for i in range(4):
        if level > 0 and path[level-1] == 'B' and cards[i] == 'T':
            continue
        if level > 0 and path[level-1] == 'T' and cards[i] == 'B':
            continue
        path[level] = cards[i]
        abc(level+1)
        path[level] = ''

abc(0)
print(cnt)
