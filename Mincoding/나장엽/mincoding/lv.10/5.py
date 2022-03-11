n = int(input())


arr = [[0]*3 for _ in range(3)]
if n % 5 == 1:
    a = 1
    for i in range(2, -1, -1):
        for k in range(2, -1,-1):
            arr[k][i] = a
            a += 1
if n % 5 == 2:
    b = 1
    for i in range(2, -1, -1):
        for k in range(0, 3, 1):
            arr[i][k] = b
            b += 1
if n % 5 != 1 and n % 5 != 2:
    c = 10
    for i in range(0, 3, 1):
        for k in range(0, 3, 1):
            arr[k][i] = c 
            c += 1
            
for i in range(3):
    for k in range(3):
        print(arr[i][k], end= ' ')
    print()