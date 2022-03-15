arr = [list(map(int, input().split())) for _ in range(3)]
sum = 0
for i in range(3):
    for k in range(0, i+1, 1):
        sum += arr[i][k]
print(sum)