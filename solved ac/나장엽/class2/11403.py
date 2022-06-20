# 가중치 없는 방향 그래프 g가 주어졌을 때 모든 정점(y, x)에 대해서 y에서 x로 가는 경로가 있는지 없는지 구하는 프로그램을 작성해라
from collections import deque
import sys
input = sys.stdin.readline

def BFS(idx):
    visited = [0] * N
    que = deque([idx])
    while que:
        index = que.popleft()
        for i, v in enumerate(graph[index]):
            if visited[i] == 0 and v == 1:
                visited[i] = 1
                que.append(i)
    return visited




N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
for idx in range(N):
    print(' '.join(map(str, BFS(idx))))