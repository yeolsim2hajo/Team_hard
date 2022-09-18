n = int(input())
arr = [[0]*4 for _ in range(4)]

if n % 2 == 0:
    a = 1
    for i in range(4):
        arr[i][i] = a
        a += 1
else:
    b = 1
    idx = 0
    for i in range(3,-1,-1):
        arr[idx][i] = b
        b += 1
        idx += 1
        
for i in range(4):
    for k in range(4):
        print(arr[i][k], end=' ')
    print()