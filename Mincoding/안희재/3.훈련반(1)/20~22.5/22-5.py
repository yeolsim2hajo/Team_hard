friends = [1,2,3,4]
n = int(input())
path = [''] * 4

# 브랜치는 총 n개
# 레벨은 4 , path도 크기는 4

def abc(level):
    if level == 4:
        for i in range(4):
            print(path[i], end='')
        print()
        return

    for i in range(n):
        path[level] = friends[i]
        abc(level+1)

abc(0)