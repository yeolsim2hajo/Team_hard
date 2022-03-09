arr = [[0] * 4 for _ in range(2)]

num = list(map(int,input().split()))

arr[num[0]][num[1]] = 1

for i in range(2):
    print(*arr[i])