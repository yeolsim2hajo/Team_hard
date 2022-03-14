def bbq(level):
    if level == num + 6:
        print(level, end= ' ')
        return

    bbq(level+2)
    print(level, end= ' ')


num = int(input())
bbq(num)