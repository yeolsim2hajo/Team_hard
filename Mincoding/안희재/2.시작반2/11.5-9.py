num = list(map(int,input().split()))
num1 = num[::-1]
tmp = 0
arr = [[0] * 3 for _ in range(2)]

for i in range(2):
    for j in range(3):
        arr[i][j] = num1[tmp]
        tmp += 1

arr[0][0], arr[1][2] = arr[1][2], arr[0][0]

for i in range(2):
    print(*arr[i], end= ' ')
