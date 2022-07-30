# 백준 16956 늑대와 양

import sys
input = sys.stdin.readline
r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]
ans = 1
def abc(y, x):
    global ans
    directy = [0, 0, -1, 1]
    directx = [-1, 1, 0, 0]
    for k in range(4):
        dy = directy[k] + y
        dx = directx[k] + x
        if dy<0 or dx<0 or dy>=r or dx>=c:
            continue
        if arr[dy][dx] == 'S':
            ans = 0
            break
        elif arr[dy][dx] == '.':
            arr[dy][dx] = 'D'
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'W':
            abc(i, j)
            if ans == 0:
                break
if ans == 0:
    print(ans)
else:
    print(ans)
    for i in range(r):
        for j in range(c):
            print(arr[i][j], end="")
        print()