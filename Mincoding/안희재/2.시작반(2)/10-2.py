num = int(input())

arr = [[0] * 4 for _ in range(4)]

if num % 2:
    for i in range(4):
        arr[i][3-i] = i+1
else:
    for i in range(4):
        arr[i][i] = i+1

for i in range(4):
    print(*arr[i])