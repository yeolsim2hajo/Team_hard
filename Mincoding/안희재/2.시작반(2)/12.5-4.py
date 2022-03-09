arr = [[0] * 5 for _ in range(5)]
num = int(input())

for i in range(5):
    for j in range(5):
        if i != 0 and i != 4 and j != 0 and j != 4:
            arr[i][j] = '_'
        else:
            arr[i][j] = num

for i in range(5):
    print(*arr[i],sep='')

