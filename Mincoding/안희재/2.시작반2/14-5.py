arr = [list(map(int,input().split())) for _ in range(3)]

sum = 0
for i in range(3):
    for j in range(i+1):
        sum += arr[i][j]

print(sum)