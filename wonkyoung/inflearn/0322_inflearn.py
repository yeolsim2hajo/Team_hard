#72 너비 우선 탐색
# graph = {'E': set(['D','A']),
#          'F': set(['D']),
#          'A': set(['E', 'C','B']),
#          'B': set(['A']),
#          'C': set(['A']),
#          'D': set(['E','F'])}
#
# def bfs(graph,start):
#     visited = []
#     queue = [start]
#     while queue:
#         n = queue.pop(0)
#         if n not in visited:
#             visited.append(n)
#             queue += graph[n] - set(visited)
#     return visited
#
# print(bfs(graph,'E'))


#73 최단 경로 찾기
# graph = {'A': set(['B','C']),
#          'B': set(['A','D','E']),
#          'C': set(['A', 'F']),
#          'D': set(['B']),
#          'E': set(['B','F']),
#          'F': set(['C','E'])}
#
# def find(start,end):
#     q = []
#     q.append(graph[start])
#     cnt = -1
#     min_val = 100
#     while q:
#         node = q.pop(0)
#         cnt += 1
#         new = graph[node]
#             if new == end:
#                 print(min(cnt,min_val))
#                 return
#             q.append(new)
#
# a, b = input().split()
# find(a,b)
