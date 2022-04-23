A = [2,1,2,4,5]
B = [[2,5,3], [4,5,7], [8,7,2]]

num = int(input())

cnt = 0
for i in A:
    if i == num:
        cnt += 1

for i in range(3):
    for j in range(3):
        if B[i][j] == num:
            cnt += 1

print(cnt)    