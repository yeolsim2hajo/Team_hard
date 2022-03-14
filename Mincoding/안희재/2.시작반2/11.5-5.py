num = input().split()
arr = [[0] * 3 for _ in range(2)]
tmp = 0

for i in range(6):
    if num[i] == '0':
        num[i] = '#'

for i in range(2):
    for j in range(3):
        arr[i][j] = num[tmp]
        tmp += 1

for i in range(2):
    print(*arr[i],sep='')