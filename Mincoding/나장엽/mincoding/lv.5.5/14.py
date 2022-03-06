from re import A


arr = [0]*6

a, b = map(int, input().split())

for i in range(0, b-a+1, 1):
    arr[i] = a
    a += 1
    print(arr[i], end = '')