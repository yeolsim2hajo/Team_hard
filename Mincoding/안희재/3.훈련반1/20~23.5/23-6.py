cards = input()
list = [i for i in cards]
path = [''] * 4 # 4장이므로, n=4
cnt = 0

def abc(level):
    if level == 4:
        global cnt
        cnt += 1
        return
    
    for i in range(5):
        if level > 0 and abs(int(path[level-1]) - int(list[i])) > 3:
            continue
        path[level] = list[i]
        abc(level+1)

abc(0)
print(cnt)