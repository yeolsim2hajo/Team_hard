#221221
# import sys
# new_input = sys.stdin.readline
# R, C = map(int, new_input().split())
# block = [new_input().split() for _ in range(R)]
# N = int(new_input())
# rules = [tuple(map(int, new_input().split())) for _ in range(N)]
# steps = -1
# from collections import deque
# q = deque()
# visited = [[1000] * C for _ in range(R)]
# for j in range(C):
#     if block[0][j] == '1':
#         q.append((0, j, 0))
#         visited[0][j] = 0
# while q:
#     r, c, cnt = q.popleft()
#     if r == R-1:
#         steps = cnt
#         break
#     for dr, dc in rules:
#         nr, nc, new_cnt = r+dr, c+dc, cnt+1
#         if 0 <= nr < R and 0 <= nc < C:
#             if block[nr][nc] == '1' and visited[nr][nc] >= new_cnt:
#                 visited[nr][nc] = new_cnt
#                 q.append((nr, nc, new_cnt))
# print(steps)


# heap
import sys
new_input = sys.stdin.readline
R, C = map(int, new_input().split())
block = [new_input().split() for _ in range(R)]
N = int(new_input())
rules = [tuple(map(int, new_input().split())) for _ in range(N)]
steps = -1
from heapq import heappop, heappush
heap = []
visited = [[1000] * C for _ in range(R)]
for j in range(C):
    if block[0][j] == '1':
        heappush(heap, (0, 0, j))
        visited[0][j] = 0
while heap:
    r, cnt, c = heappop(heap)
    if -r == R-1:
        steps = cnt
        break
    for dr, dc in rules:
        nr, nc, new_cnt = -r+dr, c+dc, cnt+1
        if 0 <= nr < R and 0 <= nc < C:
            if block[nr][nc] == '1' and visited[nr][nc] >= new_cnt:
                visited[nr][nc] = new_cnt
                heappush(heap, (-nr, new_cnt, nc))
print(steps)

