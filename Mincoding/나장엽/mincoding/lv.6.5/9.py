arr = [5,4,1,2,7,8]

n = int(input())
for k in range(n):
    for i in range(len(arr)-1, -1, -1):
        print(arr[i], end= ' ')
    print()