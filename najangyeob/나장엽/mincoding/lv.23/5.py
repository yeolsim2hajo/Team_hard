arr = ['E','W','A','B','C']
path = ['']*4
str = input()
used = [0]*5
def abc(level):
    global str
    if level == 4:
        for i in range(4):
            print(path[i], end='')
        print()
        return

    for i in range(5):
        if arr[i] == str:
            continue
        if used[i] == 0:
            path[level] = arr[i]
            used[i] = 1
            abc(level+1)
            used[i] = 0
            path[level] = ''

abc(0)
