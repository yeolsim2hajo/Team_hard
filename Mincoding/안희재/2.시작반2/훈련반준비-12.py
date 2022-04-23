arr = [[0] * 4 for _ in range(4)]
num = int(input())

tmp = num
for i in range(4):
    if i == 0 or i == 2: # 순서대로
        for j in range(4):
            arr[i][j] = tmp
            tmp += 1
    else: # 거꾸로
        for j in range(3,-1,-1):
            arr[i][j] = tmp
            tmp += 1

for i in range(4):
    print(*arr[i])