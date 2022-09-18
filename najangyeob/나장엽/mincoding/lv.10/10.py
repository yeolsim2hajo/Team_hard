n = int(input())

arr = [[0]*4 for _ in range(3)]

a = 1
for i in range(2, -1, -1):
    for k in range(3, -1, -1):
        arr[i][k] = a
        a += 1
for i in range(3):
    arr[i][n] = 0
    
for i in range(3):
    for k in range(4):
        print(arr[i][k], end= ' ')
    print()