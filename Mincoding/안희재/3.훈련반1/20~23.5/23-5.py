members = ['E','W','A','B','C']
zero = input()
path = [''] * 4
used = [0] * 5

idx = 0
for i in range(len(members)):
    if members[i] == zero:
        idx = i
used[idx] = 1

def abc(level):
    if level == 4:
        for i in range(4):
            print(path[i], end= '')
        print()
        return

    for i in range(5):
        if used[i] == 1:
            continue
        path[level] = members[i]
        used[i] = 1
        abc(level+1)
        used[i] = 0

abc(0)