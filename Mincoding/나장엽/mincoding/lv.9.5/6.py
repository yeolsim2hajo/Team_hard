arr = [
    [3,5,14],
    [2,3,9],
    [6,2,7]
]

n = int(input())

cnt = 0
for i in range(len(arr)):
    for k in range(len(arr[i])):
        if arr[i][k] % n == 0:
            cnt += 1

print(cnt)