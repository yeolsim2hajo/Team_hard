arr = [[0 for col in range(4)] for j in range(7)]

num = 1
for i in range(7):
    for j in range(4):
        arr[i][j] = num
        num += 1

n = list(map(int, input().split()))

for k in range(0, 3):
    for g in range(0, 4):
        arr[n[k]][g] = 0

for p in range(0, 7):
    for l in range(0, 4):
        print(arr[p][l], end=' ')
    print()