arr = [0] * 4

num = list(map(int,input().split()))

arr[0] = num[0]
arr[2] = num[1]

for i in range(4):
    print(arr[i],end='')