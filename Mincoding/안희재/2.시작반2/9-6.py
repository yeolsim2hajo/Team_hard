arr = [[''] * 3 for _ in range(3)]
tmp = 65
for i in range(3):
    for j in range(3):
        arr[i][j] = chr(tmp)
        tmp += 1

x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())

arr[x1][y1], arr[x2][y2] = arr[x2][y2], arr[x1][y1]

for i in range(3):
    print(*arr[i], sep = '')