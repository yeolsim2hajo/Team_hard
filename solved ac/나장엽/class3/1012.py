# 지렁이가 한마리가 있으면 인접한 다른 배추로 이동할 수 있음
# 상 하 좌 우 네 방향에 다른 배추가 위치한 경우 서로 인접.
# BFS
# 1을 발견하면 BFS 수행 -> 1을 0으로 재할당 -> 한 구역의 BFS가 끝나면 그 구역은 0으로 변경
# 1을 발견하면 카운트를 +1 

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = int(input())

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(t):
    cnt = 0
    n, m, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)