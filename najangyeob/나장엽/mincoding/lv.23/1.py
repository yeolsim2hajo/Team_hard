name = list(input())
path = ['']*4
used = [0]*4

def abc(level):
    if level == 3:
        for i in range(3):
            print(path[i], end= '')
        print()
        return

    for i in range(4):
        if used[i] == 0:
            path[level]= name[i]
            used[i] = 1
            abc(level+1)
            path[level] = ''
            used[i] = 0
abc(0)