arr = [[3,5,4,1],[1,1,2,3],[6,7,1,2]]
lst = list(map(int, input().split())) 

for i in range(3):
    for k in range(4):
        if arr[i][k] == lst[0]:
            arr[i][k] = lst[1]
        elif arr[i][k] == lst[1]:
            arr[i][k] = lst[2]
        elif arr[i][k] == lst[2]:
            arr[i][k] = lst[3]
        elif arr[i][k] == lst[3]:
            arr[i][k] = lst[0]

for i in range(3):
    print(*arr[i], sep=' ')