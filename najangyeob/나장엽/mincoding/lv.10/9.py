arr = [[0]*4 for _ in range(4)]

a = 1
for i in range(3, -1, -1):
    for k in range(0, 4, 1):
        arr[k][i] = a
        a += 1
        
        
for i in range(4):
    for k in range(4):
        print(arr[i][k], end = ' ')
    print()