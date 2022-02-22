def bbq(level):
    if level == 0:
        print(level, end= ' ')
        return

    print(level, end= ' ')
    bbq(level-1)
    print(level, end= ' ')



num = int(input())

bbq(num)
