arr = [[3,5,14], [2,3,9], [6,2,7]]
num = int(input())

cnt = 0
for i in range(3):
    for j in range(3):
        if arr[i][j] % num == 0:
            cnt += 1

print(cnt)