arr = [[3,4,1,6], [3,5,3,6], [0,0,0,0], [5,4,6,0]]

num = list(map(int,input().split()))
for i in range(4):
    arr[2][i] = num[i]

max, min = 0, 2e18
a, b = 0, 0 # max좌표
c, d = 0, 0 # min좌표

for i in range(4):
    for j in range(4):
        if max < arr[i][j]:
            max = arr[i][j]
            a, b = i, j
        if min > arr[i][j]:
            min = arr[i][j]
            c, d = i, j

print(f'MAX={max}({a},{b})')
print(f'MIN={min}({c},{d})')
