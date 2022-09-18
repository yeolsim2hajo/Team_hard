n = int(input())

def abc(level, num):
    if num == 0:
        return

    abc(level+1, num//2)
    print(num, end= ' ')
abc(0, n)