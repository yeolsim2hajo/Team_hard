n = int(input()) # 입력받는 level
card = ['B', 'G', 'T', 'K']
path = [''] * n

def abc(level):
    if level == n:
        for i in range(len(path)):
            print(path[i], end='')
        print()
        return

    for i in range(4):
        path[level] = card[i]
        abc(level+1)

abc(0)