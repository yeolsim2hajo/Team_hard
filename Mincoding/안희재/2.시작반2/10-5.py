num = int(input())
arr = [[0] * 3 for _ in range(3)]

if num % 5 == 1:
    x, y = 9, 3
    for i in range(3):
        for j in range(3):
            arr[i][j] = x-y*j
        x -= 1

elif num % 5 == 2:
    x, y = 7, 1
    for i in range(3):
        for j in range(3):
            arr[i][j] = x+y*j
        x -= 3
else:
    x, y = 10,3
    for i in range(3):
        for j in range(3):
            arr[i][j] = x+y*j
        x += 1

for i in range(3):
    print(*arr[i])