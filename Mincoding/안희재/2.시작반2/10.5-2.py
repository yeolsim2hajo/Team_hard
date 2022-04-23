num = int(input())
arr = [[0] * 5 for _ in range(5)]

tmp = 21
for i in range(5):
    for j in range(5):
        arr[i][j] = tmp + i - 5*j

for i in range(5):
    arr[num][i] = num

for i in range(5):
    print(*arr[i])
