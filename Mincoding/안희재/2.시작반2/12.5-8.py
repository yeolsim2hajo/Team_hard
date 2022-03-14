arr = [[0] * 3 for _ in range(3)]
num = int(input())

for i in range(3):
    for j in range(2-i,3):
        arr[i][j] = num
        num += 1

for i in range(3):
    print(*arr[i],sep='')