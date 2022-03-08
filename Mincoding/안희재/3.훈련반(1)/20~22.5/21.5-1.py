arr = [input() for _ in range(4)]

A_x, A_y = (0, 0)
B_x, B_y = (0, 0)
for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A':
            A_x, A_y = i, j
        if arr[i][j] == 'B':
            B_x, B_y = i, j

print(abs(A_x-B_x)+abs(A_y-B_y))