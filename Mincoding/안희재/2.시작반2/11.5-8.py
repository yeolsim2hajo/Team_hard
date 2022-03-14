arr = [[3,1,6], [7,8,4], [9,2,3]]
a, b, c = map(int,input().split())

arr[a][b] = c
min = 2e18
max = 0

for i in range(3):
    for j in range(3):
        if min > arr[i][j]:
            min = arr[i][j]
        if max < arr[i][j]:
            max = arr[i][j]

print(max+min)