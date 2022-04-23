n = int(input())

arr = [[0]*4 for _ in range(3)]

for i in range(3):
    for k in range(4):
        if i == 0:
            if k >=2:
                arr[i][k] = n
                n+=1
        if i == 1:
            if k >= 1:
                arr[i][k] = n
                n+=1

        if i == 2:
            arr[i][k] = n
            n += 1

for i in range(3):
    for k in range(4):
        if arr[i][k] == 0:
            print(' ', end='')
        else: 
            print(arr[i][k], end= '')
    print()