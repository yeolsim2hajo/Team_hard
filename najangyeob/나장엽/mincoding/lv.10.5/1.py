arr = [[0]*4 for _ in range(4)]

n = 2
for i in range(4):
    for k in range(4):
        arr[k][i] = n
        n += 2        

for i in range(4):
    print(*arr[i], sep=' ')