num = list(map(int,input().split()))

arr = [[0] * 2 for _ in range(3)]

tmp = 0
for i in range(3):
    for j in range(2):
        arr[i][j] = num[tmp] + 2
        tmp += 1

for i in range(3):
    print(*arr[i])