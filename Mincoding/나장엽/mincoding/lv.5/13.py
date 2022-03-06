arr = [3,4,1,5,8,1,7,7,3,6,9]

n = int(input())


for i in range(0, len(arr), n):
    print(arr[i], end = ' ')