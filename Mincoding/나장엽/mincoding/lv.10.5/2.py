arr = [[0]*5 for _ in range(5)]
n = 1
for i in range(4, -1, -1):
    for k in range(5):
        arr[k][i] = n
        n += 1

target = int(input())
for i in range(5):
    arr[target][i] = target
    
for i in range(5):
    print(*arr[i], sep= ' ')