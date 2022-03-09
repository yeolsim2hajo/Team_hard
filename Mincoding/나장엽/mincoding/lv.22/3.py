path = ['']*2
sign = ['B','G','T','K']
n = int(input())

def abc(level):
    global n
    if level == n:
        for i in range(n):
            print(path[i], end='')
        print()
        return
    
    for i in range(4):
        path[level] = sign[i]
        abc(level+1)

abc(0)
