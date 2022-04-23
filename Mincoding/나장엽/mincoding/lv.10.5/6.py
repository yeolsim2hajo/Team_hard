n = 10
arr = [[0]*3 for _ in range(6)]

for i in range(3):
    for k in range(6):
        arr[k][i] = n
        n += 1
        
a, b = map(int, input().split())

for i in range(a, b+1):
    for k in range(3):
        arr[i][k] = 7

for i in range(6):
    print(*arr[i], sep=' ')
        