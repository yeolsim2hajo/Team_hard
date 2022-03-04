arr = list(map(int, input().split()))


for i in range(4, 0, -1):
    for k in range(0, len(arr)-i+1):
        print(arr[k], end= ' ')
    print()