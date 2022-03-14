arr = []
for i in range(2):
    num = list(map(int,input().split()))
    arr.append(num)

arr2 = []
for i in range(2):
    for j in range(3):
        arr2.append(arr[i][j])

arr2.sort()
tmp = 0
for i in range(2):
    for j in range(3):
        arr[i][j] = arr2[tmp]
        tmp += 1

for i in range(2):
    print(*arr[i])