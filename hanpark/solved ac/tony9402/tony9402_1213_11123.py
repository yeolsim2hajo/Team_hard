# 백준 11123 양 한마리... 양 두마리...

import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
directy, directx = [0, 0, -1, 1], [-1, 1, 0, 0]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    arr[x][y] = '.'
    while q:
        x, y = q.popleft()
        for z in range(4):
            dy = y + directy[z]
            dx = x + directx[z]
            if (0 <= dx < h) and (0 <= dy < w) and arr[dx][dy] == '#':
                q.append((dx, dy))
                arr[dx][dy] = '.'
for _ in range(T):
    h, w = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '#':
                bfs(i, j)
                ans += 1
    print(ans)