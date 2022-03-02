n = int(input())

def abc(level):
    global n
    print(level, end='')
    if level == n:
        return

    for i in range(2):
        abc(level+1)



abc(0)


