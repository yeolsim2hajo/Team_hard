arr = [0]*4


n = int(input())


for k in range(0, 4, 1):
    arr[k] = n
    n = n - 1
    print(arr[k], end= ' ')