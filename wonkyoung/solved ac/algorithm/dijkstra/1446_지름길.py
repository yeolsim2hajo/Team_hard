#221015
# import heapq
# from heapq import heappush, heappop
# N, D = map(int, input().split())
# short_path = [[] for _ in range(D)]
# for _ in range(N):
#     start, end, distance = map(int, input().split())
#     if start < D and end < D:
#         short_path[start].append((distance + start - end, end, distance))
# result = [D] * (D+1)
#
# def dijkstra(start):
#     result[start] = 0
#     heap = []
#     heappush(heap, (0, start, start, 0))
#
#     while heap:
#         dif, via, dist, distance = heappop(heap)
#         if distance > result[via]:
#             continue
#         for i in short_path[via]:
#             # 시작점(via) -> 경유지 -> 도착지
#             new_distance = via + distance + D - dist
#             if new_distance < result[i[1]]:
#                 result[i[1]] = new_distance
#                 heapq.heappush(heap, ())

# from collections import defaultdict
# 연결 관계
# match = defaultdict(list)

# 일단 풀자 - 틀림
# from pprint import pprint
# from heapq import heappush, heappop
# N, D = map(int, input().split())
# graph = []
#
# # 출발지(0)에서 각 도착지까지 거리
# result = list(range(D+1))
# result[0] = 0
# visited = []
#
# for _ in range(N):
#     start, end, distance = map(int, input().split())
#     heappush(graph, (start, end, distance))
# # 갱신
# def renew(end):
#     for dist in range(1, end):
#         for via in range(1, dist):
#             if result[dist] > result[via] + dist-via:
#                 result[dist] = result[via] + dist-via
#     return end
#
# backup = graph[:]
# for _ in range(N):
#     start, end, distance = heappop(graph)
#     if end <= D:
#         # result[start] 최솟값 찾기
#         already = renew(start)
#         visited.append(start)
#         # 갱신
#         if result[end] > result[start] + distance:
#             result[end] = result[start] + distance
#             # for i in range(end, D):
#             #     result[i] = result[end] + D-end
#
# for i in range(1,D):
#     result[D] = min(result[D], result[i]+D-i)
# print(result[D])




#221016
# from heapq import heappush, heappop
# from collections import defaultdict
# N, D = map(int, input().split())
# heap = []
# short_path = defaultdict(list)
# result = list(range(D+1))
# for _ in range(N):
#     start, end, distance = map(int, input().split())
#     new_distance = result[start] + distance
#     if result[end] > new_distance:
#         short_path[start].append((end, distance))
#         result[end] = new_distance
#
#
# while heap:
#
#
# for start, value in short_path.items():
#     for end, distance in value:
#         if end > D:
#             continue
#         curve = end - start
#         if curve >= result[end]:



# heap에 다 넣기(heapq)
# 순서대로 dict에 갱신
# 돌면서 최솟값 찾기


#221023
#dfs
N, D = map(int, input().split())
short_path = [list(map(int, input().split())) for _ in range(N)]
min_drive = 10000

def dfs(end, total):
    for j in range(N):
        new_start, new_end, new_total = short_path[j]
        if new_start == end:
            dfs(new_end, total + new_total)
        elif new_start > end:
            pass

for i in range(N):
    start, end, total = short_path[i]
    if start:
        total += start
    dfs(end, total)









