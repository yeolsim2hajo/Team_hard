n = input()

arr = [[0]*5 for _ in range(5)]

for i in range(5):
    for k in range(5):
        if i == 0 or i == 4 or k == 0 or k == 4:
            arr[i][k] = n
        else:
            arr[i][k] = '_'
        print(arr[i][k], end= '')
    print()