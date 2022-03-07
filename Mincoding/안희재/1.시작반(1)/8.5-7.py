arr = [[0] * 3 for _ in range(3)]

a = list(map(int,input().split()))

arr[a[0]][a[1]] = a[2]

for i in range(3):
    print(*arr[i])