arr = [list(input()) for _ in range(4)]

for i in range(4):
    for k in range(3):
        if arr[i][k] == 'A':
            y1, x1 = i, k
        if arr[i][k] == 'B':
            y2, x2 = i, k


print(abs(x1-x2+y1-y2))