from re import L


arr = [
    [3,5,4,2,5],
    [3,3,3,2,1],
    [3,2,6,7,8],
    [9,1,1,3,2]
]

s1, s2 = map(int, input().split())

def find(y, x):
    sum = 0
    for i in range(s1):
        for k in range(s2):
            if 0 <= y+i < 4 and 0 <= x+k < 5:
                sum += arr[y+i][x+k]
    return sum

max = 0
idx_y = 0
idx_x = 0
for i in range(4):
    for k in range(5):
        if max < find(i, k):
            max = find(i, k)
            idx_y = i
            idx_x = k

print('({},{})'.format(idx_y, idx_x))
        