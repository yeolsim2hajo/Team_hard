arr = [list(input()) for _ in range(2)]

char = ['']*12

idx = 0
for i in range(len(arr)):
    for k in range(len(arr[i])):
        char[idx] = arr[i][k]
        idx += 1


for i in range(len(char)):
    print(char[i], end='')