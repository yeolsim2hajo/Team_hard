# 백준 1743 음식물 피하기

import sys
from collections import deque
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr, check = [[0]*m for _ in range(n)], [[0]*m for _ in range(n)]
for _ in range(k):
    y, x = map(int, input().split())
    arr[y-1][x-1] = 1
ans = 0
def abc(y, x):
    global ans
    q = deque()
    q.append([y, x])
    rst = 1
    while q:
        nowy, nowx = q.popleft()
        directy = [0, 0, -1, 1]
        directx = [-1, 1, 0, 0]
        for z in range(4):
            dy = nowy + directy[z]
            dx = nowx + directx[z]
            if dy < 0 or dx < 0 or dy >= n or dx >= m:
                continue
            if arr[dy][dx] == 1 and check[dy][dx] == 0:
                check[dy][dx] = 1
                rst += 1
                q.append([dy, dx])
    if rst > ans:
        ans = rst
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and check[i][j] == 0:
            check[i][j] = 1
            abc(i, j)
print(ans)