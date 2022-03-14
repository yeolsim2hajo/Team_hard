arr = [[0] * 4 for _ in range(4)]

x, y = 13,4
for i in range(4):
    for j in range(4):
        arr[i][j] = x - y*j
    x += 1

for i in range(4):
    print(*arr[i])