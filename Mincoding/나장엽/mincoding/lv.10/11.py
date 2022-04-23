arr = [list(map(int, input().split())) for _ in range(4)]
for i in range(4):
    for k in range(4):
        if arr[i][k]%2 == 1:
            arr[i][k] = '@'
        elif arr[i][k] == 0:
            arr[i][k] = '!'
        elif arr[i][k]%2 == 0:
            arr[i][k] = '#'

for i in range(4):
    for k in range(4):
        print(arr[i][k], end = '')
    print()