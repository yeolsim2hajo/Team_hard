word = input().split()

arr = [[''] * 6 for _ in range(3)]

for i in range(3):
    for j in range(6):
        if j < 4:
            arr[i][j] = word[0]
        else:
            arr[i][j] = word[1]

for i in range(3):
    print(*arr[i],sep='')