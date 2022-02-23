n = int(input())

answer = ['x', 'o']
path = [''] * n

def abc(level):
    if level == n:
        for i in range(n):
            print(path[i], end='')
        print()
        return

    for i in range(2):
        path[level] = answer[i]
        abc(level+1)

abc(0)
