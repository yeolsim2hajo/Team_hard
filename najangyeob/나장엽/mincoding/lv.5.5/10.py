n = int(input())

arr = [0]*6
k = 1
for i in range(len(arr)):
    arr[i] = n*k
    k += 1
    print(arr[i], end = ' ')