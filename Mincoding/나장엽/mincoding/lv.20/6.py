n1, n2 = map(int, input().split())

def abc(level, num):
    global n2
    global n1
    print(num, end=' ')
    if level == (n2 - n1):
        num = num-1
        return num

    abc(level+1, num+1)
    print(num, end= ' ')
abc(0, n1)