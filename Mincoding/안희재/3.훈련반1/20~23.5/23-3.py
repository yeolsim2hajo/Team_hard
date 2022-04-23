n = int(input())
type = ['A', 'B', 'C']
path = [''] * n
cnt = 0

def abc(level):
    if level == n:
        global cnt
        cnt += 1
        return
    
    for i in range(3):
        if level > 1 and path[level-2] == path[level-1] == type[i]:
            continue
        path[level] = type[i]
        abc(level+1)
        path[level] = ''

abc(0)
print(cnt)