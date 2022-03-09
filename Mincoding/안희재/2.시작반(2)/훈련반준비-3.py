arr = [[0] * 4 for _ in range(3)]
num = int(input())

tmp = 12
for i in range(3):
    for j in range(4):
        arr[i][j] = tmp-j
    tmp -= 4

if num == 1:
    for i in range(4):
        arr[0][i] = 7
elif num == 2:
    for i in range(4):
        arr[1][i] = 7
else:
    for i in range(4):
        arr[2][i] = 7
        
for i in range(3):
    print(*arr[i])