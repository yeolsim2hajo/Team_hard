# 최소 시간 출력
# BFS
# x - 1, x + 1, 2 * x -> 세번 BFS 돌려서 찾는 시간을...?
import sys
from collections import deque
input = sys.stdin.readline


def bfs(n):
    que = deque([n])
    while que:
        n = que.popleft()
        if n == k:
            return visited[n]
        for i in (n-1, n+1, 2*n):
            if 0 <= i <= 100  and not visited[i]:
                visited[i] = visited[n] + 1
                que.append(i)


n, k = map(int, input().split())
visited = [0 for _ in range(100)]
print(bfs(n))
print(visited)