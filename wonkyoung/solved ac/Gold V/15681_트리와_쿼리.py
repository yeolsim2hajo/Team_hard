#230112
# bfs - 시간 초과
# import sys
# from collections import deque
#
# new_input = sys.stdin.readline
# N, R, Q = map(int, new_input().split())
# node_info = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     node_1, node_2 = map(int, new_input().split())
#     node_info[node_1].append(node_2)
#     node_info[node_2].append(node_1)
# q = deque()
# q.append((R, 0))
# visited = [False] * (N+1)
# levels = [set() for _ in range(N)]
# visited[R] = True
# levels[0].add(R)
# while q:
#     root, level = q.popleft()
#     level += 1
#     i = 0
#     while i < len(node_info[root]):
#         node = node_info[root][i]
#         if not visited[node]:
#             visited[node] = True
#             levels[level].add(node)
#             q.append((node, level))
#             i += 1
#         else:
#             node_info[root].remove(node)
# for _ in range(Q):
#     new_root = int(new_input())
#     cnt = 1
#     q.append(new_root)
#     while q:
#         node = q.popleft()
#         cnt += len(node_info[node])
#         q.extend(node_info[node])
#     print(cnt)

#
import sys
from collections import deque

new_input = sys.stdin.readline
N, R, Q = map(int, new_input().split())
node_info = [[] for _ in range(N+1)]
for _ in range(N-1):
    node_1, node_2 = map(int, new_input().split())
    node_info[node_1].append(node_2)
    node_info[node_2].append(node_1)
q = deque()
q.append((R, 0))
visited = [False] * (N+1)
visited[R] = True
tree_info = [[] for _ in range(N+1)]
while q:
    root, level = q.popleft()
    level += 1
    i = 0
    for node in node_info[root]:
        if not visited[node]:
            tree_info[root].append(node)
            visited[node] = True
            q.append((node, level))
            i += 1

for _ in range(Q):
    new_root = int(new_input())
    cnt = 1
    q.append(new_root)
    while q:
        node = q.popleft()
        cnt += len(node_info[node])
        q.extend(node_info[node])
    print(cnt)

