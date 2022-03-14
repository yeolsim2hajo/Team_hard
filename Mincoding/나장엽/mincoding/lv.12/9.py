from pyrsistent import b


str = input()
arr = [[0]*3 for _ in range(3)]

if ord('0') <= ord(str) <= ord('9'):
    n = 1
    for i in range(2, -1, -1):
        for k in range(2, -1, -1):
            if i == 2:
                if k >= 2:
                    arr[i][k] = n
                    n += 1
            if i == 1:
                if k >= 1:
                    arr[i][k] = n
                    n += 1
                    
            if i == 0:
                if k>=0:
                    arr[i][k] = n
                    n += 1
    for i in range(3):
        for k in range(3):
            if arr[i][k] == 0:
                print(' ', end='')
            else:
                print(arr[i][k], end='')
        print()


if ord('A') <= ord(str) <= ord('Z'):
    n = 1
    for i in range(2, -1, -1):
        for k in range(3):
            if i == 2:
                if k >= 0:
                    arr[i][k] = n
                    n += 1
            if i == 1:
                if k <= 1 :
                    arr[i][k] = n
                    n += 1
            if i == 0:
                if k < 1:
                    arr[i][k] = n
                    n += 1


    for i in range(3):
        for k in range(3):
            if arr[i][k] == 0:
                print(' ', end='')
            else:
                print(arr[i][k], end='')
        print()

