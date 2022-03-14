arr = [list(map(int,input().split())) for _ in range(5)]

for i in range(5):
    sum = 0
    for j in range(4):
        sum += arr[i][j]
    print(sum,end= ' ')
