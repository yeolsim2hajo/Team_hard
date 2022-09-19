# 백준 2178 미로 탐색

import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
arr[0][0] = 1
directy, directx = [0, 0, -1, 1], [-1, 1, 0, 0]
q = deque([[0, 0]])
while q:
    [nowy, nowx] = q.popleft()
    for i in range(4):
        dy = nowy + directy[i]
        dx = nowx + directx[i]
        if dy < 0 or dx < 0 or dy >= n or dx >= m:
            continue
        if arr[dy][dx] == '1':
            q.append([dy, dx])
            arr[dy][dx] = arr[nowy][nowx] + 1
print(arr[n-1][m-1])