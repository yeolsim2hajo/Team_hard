arr = [[0]*2 for _ in range(3)]
num = list(map(int, input().split()))

temp = 0
for i in range(3):
    for k in range(2):
        arr[i][k] = num[temp] + 2
        temp += 1
        
        
for i in range(3):
    print(*arr[i])