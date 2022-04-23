arr = [[4,5,4,5,4], [8,9,8,9,8], [1,2,1,2,1], [4,5,4,5,4], [6,7,6,7,6]]

for i in range(5):
    x, y = map(int,input().split())
    arr[x][y] += 1
    if arr[x][y] == 10:
        arr[x][y] = 0

for i in range(5):
    print(*arr[i],sep='')