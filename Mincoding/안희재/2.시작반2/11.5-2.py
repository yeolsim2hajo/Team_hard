arr = [[1,1,1], [1,2,1], [3,6,3]]

num = int(input())
cnt = 0

for i in range(3):
    for j in range(3):
        if arr[i][j] == num:
            cnt += 1

print(cnt)