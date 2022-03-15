arr = [ list(map(int, input().split())) for _ in range(5)]


result = []
for i in range(5):
    sum = 0
    for k in range(4):
        sum += arr[i][k]
    result.append(sum)


print(*result, sep=' ')