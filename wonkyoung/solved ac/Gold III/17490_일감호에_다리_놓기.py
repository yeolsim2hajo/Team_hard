#230301
# prim
# 틀림
# def link_building():
#     from sys import stdin
#     new_input = stdin.readline
#     N, M, K = map(int, new_input().split())
#     rock_cnt = [0] + list(map(int, new_input().split()))
#     def can_link():
#         from heapq import heappush, heappop
#         if M == 0:
#             return 'YES'
#         work_block = set(tuple(map(int, sorted(new_input().split()))) for _ in range(M))
#         graph = []
#         visited = [False] * (N+1)
#         # 노드 선택
#         for i in range(1, N):
#             if (i, i+1) not in work_block:
#                 visited[i] = True
#                 graph.append((0, i + 1))
#                 graph.append((rock_cnt[i], 0))
#                 break
#         else:
#             visited[N] = True
#             graph.append((0, 1))
#             graph.append((rock_cnt[N], 0))
#         cnt = rock = 0
#         # 간선 선택
#         while cnt < N - 1:
#             cost, end = heappop(graph)
#             if not visited[end]:
#                 visited[end] = True
#                 rock += cost
#                 cnt += 1
#                 if end != 0:
#                     heappush(graph, (rock_cnt[end], 0))
#                     if end != N:
#                         if (end, end+1) not in work_block:
#                             heappush(graph, (0, end+1))
#                     elif (N, 1) not in work_block:
#                         heappush(graph, (0, 1))
#                 else:
#                     for i in range(1, N+1):
#                         if not visited[i]:
#                             heappush(graph, (rock_cnt[i], i))
#         return 'YES' if rock <= K else 'NO'
#     return can_link()
# print(link_building())


# prim

# def link_building():
#     from sys import stdin
#     new_input = stdin.readline
#     N, M, K = map(int, new_input().split())
#     rock_cnt = [0] + list(map(int, new_input().split()))
#     if M == 0:
#         return 'YES'
#
#     def can_link():
#         from heapq import heappush, heappop
#         work_block = set(tuple(map(int, sorted(new_input().split()))) for _ in range(M))
#         graph = []
#         visited = [False] * (N+1)
#         # 노드 0으로 선택
#         visited[0] = True
#         for i in range(1, N):
#             heappush(graph, (rock_cnt[i], i))
#         cnt = rock = 0
#         # 간선 선택
#         while cnt < N - 1:
#             cost, end = heappop(graph)
#             if not visited[end]:
#                 visited[end] = True
#                 rock += cost
#                 cnt += 1
#                 if 1 < end < N:
#                     for i in (end-1, end):
#                         if (i, i+1) not in work_block:
#                             heappush(graph, (0, i+1))
#                 else:
#                     if (1, N) not in work_block:
#                         heappush(graph, (0, N if end == 1 else 1))
#                     if end == N:
#                         if (N-1, N) not in work_block:
#                             heappush(graph, (0, N-1))
#                     elif (1, 2) not in work_block:
#                         heappush(graph, (0, 2))
#         print(rock)
#         return 'YES' if rock <= K else 'NO'
#     return can_link()
# print(link_building())
'''
5 3 7
2 1 3 2 1
2 3
4 5
5 1
'''

#kruskal
# def link_building():
#     from sys import stdin
#     new_input = stdin.readline
#     N, M, K = map(int, new_input().split())
#     rock_cnt = [0] + list(map(int, new_input().split()))
#     work_block = set(tuple(map(int, new_input().split())) for _ in range(M))
#     if M <= 1:
#         return 'YES'
#     root_of = list(range(N+1))
#     rank = [0] * (N+1)
#     cnt = rock = 0
#
#     def find(node):
#         if root_of[node] != node:
#             root_of[node] = find(root_of[node])
#         return root_of[node]
#
#     def link(value, node1, node2):
#         nonlocal cnt, rock
#         if node1 == node2:
#             return
#         cnt += 1
#         rock += value
#         if rank[node1] > rank[node2]:
#             root_of[node2] = node1
#         else:
#             root_of[node1] = node2
#             if rank[node1] == rank[node2]:
#                 rank[node2] += 1
#
#     def union(value, node1, node2):
#         link(value, find(node1), find(node2))
#
#     for i in range(1, N):
#         if (i, i+1) not in work_block and (i+1, i) not in work_block:
#             union(0, i, i+1)
#     if (N, 1) not in work_block and (1, N) not in work_block:
#         union(0, 1, N)
#
#     graph = [(rock_cnt[i], 0, i) for i in range(1, N+1)]
#     graph.sort(key=lambda x: x[0])
#     for i in range(len(graph)):
#         union(*graph[i])
#         if cnt == N:
#             return 'YES' if rock <= K else 'NO'
#     return 'NO'
# print(link_building())
'''
5 0 9
2 1 3 2 5
'''

# kruskal
# def link_building():
#     from sys import stdin
#     new_input = stdin.readline
#     N, M, K = map(int, new_input().split())
#     rock_cnt = [0] + list(map(int, new_input().split()))
#     road_set = set((0, i, i+1) for i in range(1, N))
#     road_set.add((0, 1, N))
#     for _ in range(M):
#         node1, node2 = map(int, new_input().split())
#         if node1 > node2:
#             node1, node2 = node2, node1
#         road_set.remove((0, node1, node2))
#
#     if M <= 1:
#         return 'YES'
#     root_of = list(range(N+1))
#     rank = [0] * (N+1)
#     cnt = rock = 0
#
#     def find(node):
#         if root_of[node] != node:
#             root_of[node] = find(root_of[node])
#         return root_of[node]
#
#     def link(value, node1, node2):
#         nonlocal cnt, rock
#         if node1 == node2:
#             return
#         cnt += 1
#         rock += value
#         if rank[node1] > rank[node2]:
#             root_of[node2] = node1
#         else:
#             root_of[node1] = node2
#             if rank[node1] == rank[node2]:
#                 rank[node2] += 1
#
#     def union(value, node1, node2):
#         link(value, find(node1), find(node2))
#
#     for road in road_set:
#         union(*road)
#
#     graph = [(rock_cnt[i], 0, i) for i in range(1, N+1)]
#     graph.sort(key=lambda x: x[0])
#     for i in range(len(graph)):
#         union(*graph[i])
#         if cnt == N:
#             return 'YES' if rock <= K else 'NO'
#     return 'NO'
# print(link_building())


#
# def link_building():
#     from sys import stdin
#     new_input = stdin.readline
#     N, M, K = map(int, new_input().split())
#     if M <= 1:
#         for _ in range(2):
#             new_input()
#         return 'YES'
#     rock_cnt = [0] + list(map(int, new_input().split()))
#     work_block = set(tuple(map(int, new_input().split())) for _ in range(M))
#     root_of = list(range(N+1))
#     rank = [0] * (N+1)
#     cnt = rock = 0
#
#     def find(node):
#         if root_of[node] != node:
#             root_of[node] = find(root_of[node])
#         return root_of[node]
#
#     def link(value, node1, node2):
#         nonlocal cnt, rock
#         if node1 == node2:
#             return
#         cnt += 1
#         rock += value
#         if rank[node1] > rank[node2]:
#             root_of[node2] = node1
#         else:
#             root_of[node1] = node2
#             if rank[node1] == rank[node2]:
#                 rank[node2] += 1
#
#     def union(value, node1, node2):
#         link(value, find(node1), find(node2))
#
#     graph = [(0, i, i+1) for i in range(1, N) if (i, i+1) not in work_block and (i+1, i) not in work_block]
#     if (N, 1) not in work_block and (1, N) not in work_block:
#         graph.append((0, 1, N))
#     graph.extend([(rock_cnt[i], 0, i) for i in range(1, N+1)])
#     graph.sort(key=lambda x: x[0])
#     for i in range(len(graph)):
#         union(*graph[i])
#         if cnt == N:
#             return 'YES' if rock <= K else 'NO'
#     return 'NO'
# print(link_building())


#
# def link_building():
#     from sys import stdin
#     new_input = stdin.readline
#     N, M, K = map(int, new_input().split())
#     rock_cnt = [0] + list(map(int, new_input().split()))
#     work_block = set(tuple(map(int, new_input().split())) for _ in range(M))
#     if M <= 1:
#         return 'YES'
#     root_of = list(range(N + 1))
#     rank = [0] * (N + 1)
#     cnt = rock = 0
#     def find(node):
#         if root_of[node] != node:
#             root_of[node] = find(root_of[node])
#         return root_of[node]
#
#     def link(value, node1, node2):
#         nonlocal cnt, rock
#         if node1 == node2:
#             return
#         cnt += 1
#         rock += value
#         if rank[node1] > rank[node2]:
#             root_of[node2] = node1
#         else:
#             root_of[node1] = node2
#             if rank[node1] == rank[node2]:
#                 rank[node2] += 1
#
#     def union(value, node1, node2):
#         link(value, find(node1), find(node2))
#
#     for i in range(1, N):
#         if (i, i+1) not in work_block and (i+1, i) not in work_block:
#             union(0, i, i+1)
#     if (N, 1) not in work_block and (1, N) not in work_block:
#         union(0, 1, N)
#
#     graph = [(rock_cnt[i], 0, i) for i in range(1, N+1)]
#     graph.sort(key=lambda x: x[0])
#     i = 0
#     while cnt < N:
#         union(*graph[i])
#         i += 1
#     return 'YES' if rock <= K else 'NO'
# print(link_building())

#
# def link_building():
#     from sys import stdin
#     new_input = stdin.readline
#     N, M, K = map(int, new_input().split())
#     rock_cnt = list(enumerate(map(int, new_input().split()), start=1))
#     work_block = set(tuple(map(int, new_input().split())) for _ in range(M))
#     if M <= 1:
#         return 'YES'
#     root_of = list(range(N + 1))
#     rank = [0] * (N + 1)
#     cnt = rock = 0
#     def find(node):
#         if root_of[node] != node:
#             root_of[node] = find(root_of[node])
#         return root_of[node]
#
#     def link(value, node1, node2):
#         nonlocal cnt, rock
#         if node1 == node2:
#             return
#         cnt += 1
#         rock += value
#         if rank[node1] > rank[node2]:
#             root_of[node2] = node1
#         else:
#             root_of[node1] = node2
#             if rank[node1] == rank[node2]:
#                 rank[node2] += 1
#
#     def union(value, node1, node2):
#         link(value, find(node1), find(node2))
#
#     for i in range(1, N):
#         if (i, i+1) not in work_block and (i+1, i) not in work_block:
#             union(0, i, i+1)
#     if (N, 1) not in work_block and (1, N) not in work_block:
#         union(0, 1, N)
#     rock_cnt.sort(key= lambda x: x[1])
#     i = 0
#     while cnt < N:
#         union(rock_cnt[i][1], 0, rock_cnt[i][0])
#         i += 1
#     return 'YES' if rock <= K else 'NO'
# print(link_building())


# prim
def link_building():
    from sys import stdin
    from heapq import heappush, heappop
    new_input = stdin.readline
    N, M, K = map(int, new_input().split())
    rock_cnt = [0] + list(map(int, new_input().split()))
    if M <= 1:
        return 'YES'
    work_block = set(tuple(map(int, new_input().split())) for _ in range(M))
    graph = []
    visited = [False] * (N+1)
    # 노드 0으로 선택
    visited[0] = True
    for i in range(1, N+1):
        heappush(graph, (rock_cnt[i], i))
    cnt = rock = 0
    # 간선 선택
    while cnt < N:
        cost, end = heappop(graph)
        if not visited[end]:
            visited[end] = True
            rock += cost
            cnt += 1
            for i in (end-1, end+1):
                if 1 <= i <= N:
                    result = i
                elif i == 0:
                    result = N
                else:
                    result = 1
                if (end, result) not in work_block and (result, end) not in work_block:
                    heappush(graph, (0, result))
    return 'YES' if rock <= K else 'NO'
print(link_building())
'''
5 3 7
2 1 3 2 5
2 3
4 5
5 1
NO

5 3 7
2 1 3 2 1
2 3
4 5
5 1

5 3 9
2 1 3 2 5
2 3
4 5
5 1
'''