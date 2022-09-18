arr = [3,5,1,2,4,6,7]
a, b = map(int, input().split())


for i in range(a, b+1, 1):
    print(arr[i], end = ' ')