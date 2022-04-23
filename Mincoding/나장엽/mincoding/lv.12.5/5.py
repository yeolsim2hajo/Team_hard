arr = [
    [4,5,4,5,4],
    [8,9,8,9,8],
    [1,2,1,2,1],
    [4,5,4,5,4],
    [6,7,6,7,6]
]

for i in range(5):
    y, x = map(int, input().split())
    arr[y][x] += 1
    if arr[y][x] == 10:
        arr[y][x] = 0


for i in range(5):
    print(*arr[i], sep='')