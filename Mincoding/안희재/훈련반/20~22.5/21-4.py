num = int(input())

def abc(level):
    print(level, end= '')
    if level == num:
        return

    for i in range(2):
        abc(level+1)

abc(0)