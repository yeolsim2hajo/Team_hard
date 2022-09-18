lst = list(map(int, input().split()))

arr = [[0]*3 for _ in range(2)]
idx = 1
for i in range(2):
    for k in range(3):
        arr[i][k] = lst[-idx]
        idx += 1

result = [0]*6
idx = 0
for i in range(2):
    for k in range(3):
        result[idx] = arr[i][k]
        idx += 1

result[0], result[-1] = result[-1], result[0]

print(*result, sep= ' ')