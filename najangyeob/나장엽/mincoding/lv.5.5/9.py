from re import A


a, b  = map(int, input().split())
arr = [0]*5

for i in range(0, len(arr)):
    arr[i] = a
    a += b
    print(arr[i], end = ' ')