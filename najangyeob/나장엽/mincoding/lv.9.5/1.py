arr1 = [2,1,2,4,5]
arr2 = [[2,5,3],[4,5,7],[8,7,2]]

n = int(input())

cnt = 0
for i in range(len(arr1)):
    if arr1[i] == n:
        cnt += 1

for i in range(len(arr2)):
    for k in range(len(arr2[0])):
        if arr2[i][k] == n:
            cnt += 1

print(cnt)