arr = [[0] * 3 for _ in range(6)]

num = list(map(int,input().split()))

for i in range(3):
    for j in range(3):
        arr[i][j] = num[0]

for i in range(3,6):
    for j in range(3):
        arr[i][j] = num[1]

for i in range(6):
    print(*arr[i],sep='')