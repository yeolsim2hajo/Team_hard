arr = [[0] * 4 for _ in range(4)]

for i in range(3):
    row = list(map(int,input().split()))
    for j in range(3):
        arr[i][j] = row[j]

# 가로줄의 합
for i in range(3):
    for j in range(3):
        arr[j][3] += arr[j][i]
# 세로줄의 합
for i in range(3):
    for j in range(3):
        arr[3][j] += arr[i][j]
# 대각선의 합
for i in range(3):
    arr[3][3] += arr[i][i]

for i in range(4):
    print(*arr[i])