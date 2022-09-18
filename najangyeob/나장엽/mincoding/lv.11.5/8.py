from re import L


a, b, c = map(int, input().split())


arr = [[3,1,6],[7,8,4],[9,2,3]]

arr[a][b] = c

max = arr[0][0]
min = arr[0][0]

for i in range(3):
    for k in range(3):
        if arr[i][k] > max:
            max = arr[i][k]
        else:
            max = max
        if arr[i][k] < min:
            min = arr[i][k]
        else:
            min = min

print(max+min)