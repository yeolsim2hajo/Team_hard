#221015
# 기본
from heapq import heappop, heappush
initial, final = map(int, input().split())
N, M = map(int, input().split())
link = [[] for _ in range(N+1)]
result = [N] * (N+1)
result[initial] = 0

for _ in range(M):
    start, end = map(int, input().split())
    link[start].append(end)
    link[end].append(start)

heap = []
heappush(heap, (0, initial))

while heap:
    cost, via = heappop(heap)
    if cost > result[via]:
        continue
    for node in link[via]:
        new_cost = cost + 1
        if new_cost < result[node]:
            result[node] = new_cost
            heappush(heap, (new_cost, node))

if result[final] == N:
    result[final] = -1
print(result[final])
