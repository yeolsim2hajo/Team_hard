arr = [[0]*3 for _ in range(3)]

a, b, c = map(int, input().split())

arr[a][b] = c


for i in range(3):
    for k in range(3):
        print(arr[i][k], end = ' ')
    print()