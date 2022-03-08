arr = [[3,5,4,2,5], [3,3,3,2,1], [3,2,6,7,8], [9,1,1,3,2]]

size_x, size_y = map(int,input().split())

def board(x, y): # x, y는 좌표
    sum = 0
    for i in range(size_x):
        for j in range(size_y):
            if 0 <= x+i < 4 and 0 <= y+j < 5:
                sum += arr[x+i][y+j]
    return sum

max = 0
max_x, max_y = (0,0)
for i in range(4):
    for j in range(5):
        if max < board(i,j):
            max = board(i,j)
            max_x, max_y = (i, j)

print(f'({max_x},{max_y})')