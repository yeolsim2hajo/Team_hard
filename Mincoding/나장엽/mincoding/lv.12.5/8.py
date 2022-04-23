arr = [[0]*3 for _ in range(3)]

n = int(input())

for i in range(3):
    for k in range(3):
        if i == 0:
            if k >= 2:
                arr[i][k] = n
                n += 1
        if i == 1:
            if k >=1 :
                arr[i][k] = n
                n += 1
        if i == 2:
            if k >= 0:
                arr[i][k] = n
                n += 1
for i in range(3):
    print(*arr[i], sep='')