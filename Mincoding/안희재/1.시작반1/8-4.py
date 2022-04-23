arr = list(map(int,input().split()))

for i in range(len(arr)-1,-1,-1):
    if arr[i] == 7:
        print(arr[i],end= ' ')
        break
    else:
        print(arr[i],end= ' ')