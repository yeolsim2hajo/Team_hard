# 1//2 = 0이잖아
num = int(input())
# 0 -> 5 4 3 2 1 순으로

def bbq(level):
    if level == 1:
        print(level, end= ' ')
        return

    bbq(level//2)
    print(level, end= ' ')

bbq(num)