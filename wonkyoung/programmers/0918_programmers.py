# 양과 늑대
# def solution(info, edges):
#     length = len(info)
#     graph = [[] for _ in range(length)]
#     for parent, child in edges:
#         graph[parent].append(child)
#
#     def dfs(next, level, total):
#         nonlocal max_sheep, max_wolves
#         # print(next, level, total)
#         sheep = level - total
#         if sheep > total:
#             if max_sheep > sheep:
#                 max_sheep, max_wolves = sheep, total
#         for j in graph[next]:
#             dfs(j, level + 1, total + info[j])
#
#     sheep_cnt = []
#     for arr in [graph[0], graph[0][::-1]]:
#         max_sheep, max_wolves = 1, 0
#         for i in arr:
#             dfs(i, max_sheep + max_wolves, max_wolves)
#         sheep_cnt.append(max_sheep)
#
#     return max(sheep_cnt)