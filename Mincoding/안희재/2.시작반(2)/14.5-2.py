num = int(input())
arr = [list(map(int,input().split())) for _ in range(5)]

if num == 1:
    for i in range(5):
        for j in range(i+1):
            print(arr[i][j], end = ' ')
        print()
else:
    for i in range(5):
        for j in range(5-i):
            print(arr[i][j], end = ' ')
        print()