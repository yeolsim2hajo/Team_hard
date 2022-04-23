# 3장이니, level = 3
word = input()
cards = [word[0], word[1], word[2], word[3]]
path = [''] * 3
used = [0] * 4

def abc(level):
    if level == 3:
        for i in range(3):
            print(path[i],end='')
        print()
        return
    
    for i in range(4):
        if used[i] == 0:
            path[level] = cards[i]
            used[i] = 1
            abc(level+1)
            used[i] = 0

abc(0)
