# 백준 1926 그림

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
check = [[0]*m for _ in range(n)]
cnt,ans = 0, 0
def abc(y, x):
    global ans
    q=deque()
    q.append([y, x])
    rst = 1
    while q:
        nowy, nowx = q.popleft()
        directy = [0, 0, 1, -1]
        directx = [1, -1, 0, 0]
        for a in range(4):
            dy = nowy + directy[a]
            dx = nowx + directx[a]
            if dy<0 or dx<0 or dy>=n or dx>=m:
                continue
            if check[dy][dx]==0 and arr[dy][dx]==1:
                check[dy][dx]=1
                rst+=1
                q.append([dy, dx])
    if rst > ans:
        ans = rst
for i in range(n):
    for j in range(m):
        if arr[i][j]==1 and check[i][j]==0:
            check[i][j]=1
            cnt+=1
            abc(i, j)
print(cnt)
print(ans)