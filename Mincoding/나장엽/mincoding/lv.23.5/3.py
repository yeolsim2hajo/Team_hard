arr = [[0]*4 for _ in range(4)]

temp = [list(map(int, input().split())) for _ in range(3)]

for i in range(0, 3):
    for k in range(0, 3):
        arr[i][k] = temp[i][k]

row_sum = []
for i in range(3):
    sum = 0
    for k in range(3):
        sum += arr[i][k]
    row_sum.append(sum)

for i in range(3):
    arr[i][3] = row_sum[i]

col_sum = []
for i in range(3):
    sum = 0
    for k in range(3):
        sum += arr[k][i]
    col_sum.append(sum)

for i in range(3):
    arr[3][i] = col_sum[i]


cross_sum = 0
for i in range(3):
    cross_sum +=  arr[i][i]

arr[3][3] = cross_sum

for i in range(len(arr)):
    print(*arr[i], sep=' ')