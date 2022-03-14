arr = [[0]*4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        arr[i][j] = 2*(i+1) + 8*j

for i in range(4):
    print(*arr[i])