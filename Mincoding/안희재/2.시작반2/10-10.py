num = int(input())
arr = [[0] * 4 for _ in range(3)]

x, y = 12,1
for i in range(3):
    for j in range(4):
        arr[i][j] = x - y*j
    x -= 4

for i in range(3):
    arr[i][num] = 0

for i in range(3):
    print(*arr[i])