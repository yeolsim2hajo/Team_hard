n = int(input())
sign = []
for i in range(1, n+1):
    sign.append(i) 
path = ['']*4

def abc(level):
    if level == 4:
        for i in range(4):
            print(path[i], end='')
        print()
        return
    for k in range(n):
        path[level] = sign[k]
        abc(level+1)

abc(0)