a, b = map(int,input().split())

# 3, 9 : 3 4 5 6 7 8 !9! 8 7 6 5 4 3

def bbq(level):

    if level == b:
        print(b, end= ' ')
        return

    print(level, end= ' ')
    bbq(level+1)
    print(level, end= ' ')

bbq(a)