n = int(input())
arr = [list(map(int, input().split())) for _ in range(5)]

if n == 1:
    for i in range(5):
        for k in range(i-i, i+1, 1):
            print(arr[i][k], end= ' ')
        print()
if n == 2:
    for i in range(5):
        for k in range(0, 5-i, 1):
            print(arr[i][k], end= ' ')
        print()