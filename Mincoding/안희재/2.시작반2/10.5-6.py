arr = [[0] * 3 for _ in range(6)]

tmp = 10
for i in range(6):
    for j in range(3):
        arr[i][j] = tmp + 6*j
    tmp += 1

a, b = map(int,input().split())

for i in range(a,b+1):
    for j in range(3):
        arr[i][j] = 7

for i in range(6):
    print(*arr[i])