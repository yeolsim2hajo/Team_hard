arr = [3,9,12,15,55]

num = sum(list(map(int,input().split())))

if num > 10:
    print(arr[len(arr)-1])
else:
    print(arr[0])