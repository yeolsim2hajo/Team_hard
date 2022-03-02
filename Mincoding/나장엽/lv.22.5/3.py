from re import L


arr = [[[0,0,0],[0,0,0],[0,0,0]] for _ in range(3)]

str = input()


for i in range(3):
    for k in range(3):
        for j in range(3):
            if i == 0:
                arr[i][k][j] = chr(ord(str))
                print(arr[i][k][j], end='')
            if i == 1:
                arr[i][k][j] = chr(ord(str)+1)
                print(arr[i][k][j], end='')
            if i == 2:
                arr[i][k][j] = chr(ord(str)+2)
                print(arr[i][k][j], end='')
        print()
    print()
