level = int(input())
branch = int(input())


def abc(lv):
    global level
    global branch
    if lv == level:
        return

    for i in range(branch):
        abc(lv+1)

abc(0)