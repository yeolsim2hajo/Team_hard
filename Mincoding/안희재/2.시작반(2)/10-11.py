arr = [list(map(int,input().split())) for _ in range(4)]

for i in range(4):
    for j in range(4):
        if arr[i][j] == 0:
            arr[i][j] = '!'
        elif arr[i][j] % 2 == 0:
            arr[i][j] = '#'
        else:
            arr[i][j] = '@'

for i in range(4):
    print(*arr[i],sep='')