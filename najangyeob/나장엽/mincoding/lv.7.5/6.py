arr = [[0]*4 for _ in range(2)]

x, y = map(int, input().split())

arr[x][y] = 1

for i in range(2):
    for k in range(4):
        print(arr[i][k], end = ' ')
    print()