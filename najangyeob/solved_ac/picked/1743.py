# 제일 큰 음식물의 크기를 구하는 문제

# bfs 문제.
import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split()) # 세로, 가로, 개수
arr = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)] # 방문

for _ in range(k):
    y, x = map(int, input().split())
    arr[y-1][x-1] = 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

que = deque()
def bfs(y, x):
    global cnt
    que.append([y,x])
    visited[y][x] = 1
    cnt += 1

    while que :
        y, x = que[0][0], que[0][1]
        que.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and arr[ny][nx] == 1:
                que.append([ny, nx])
                visited[ny][nx] = 1
                cnt += 1

answer = 0
cnt = 0

for i in range(n):
    for k in range(m):
        if arr[i][k] == 1:
            bfs(i, k)
            answer = max(answer, cnt)
            cnt = 0

print(answer)