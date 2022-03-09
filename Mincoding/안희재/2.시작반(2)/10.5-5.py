arr = [[0] * 4 for _ in range(3)]
num = list(map(int,input().split()))

for i in range(3):
    for j in range(4):
        arr[i][j] = num[i]+j

for i in range(3):
    print(*arr[i])