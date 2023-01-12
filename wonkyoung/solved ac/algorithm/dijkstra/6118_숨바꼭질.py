#220930
# heapq + bfs - 틀림
# import heapq
# N, M = map(int, input().split())
# road = [[] for _ in range(N)]
# distance = [0] * (N+1)
#
# for _ in range(M):
#     start, end = sorted(map(int, input().split()))
#     road[start].append(end)
#
# heap = []
# for i in range(len(road[1])):
#     heapq.heappush(heap, (road[1][i], 1))
#
# max_distance = number = 0
# while heap:
#     next, geori = heapq.heappop(heap)
#     if geori > max_distance:
#         max_distance = geori
#         number = next
#     if distance[next] == 0:
#         distance[next] = geori
#         heapq.heappush(heap, (next, geori))
#
# print(number, max_distance, distance.count(max_distance))

# 221001
# bfs2 - 엄청 느림
# import heapq
# N, M = map(int, input().split())
# road = [[] for _ in range(N+1)]
# # 1번 헛간에서의 거리
# distance = [50000] * (N+1)
# distance[1] = 0
#
# for _ in range(M):
#     start, end = map(int, input().split())
#     road[start].append(end)
#     road[end].append(start)
#
# heap = []
# for i in range(len(road[1])):
#     heapq.heappush(heap, (1, road[1][i]))
#     distance[road[1][i]] = 1
#
# max_distance = number = 0
# while heap:
#     geori, next = heapq.heappop(heap)
#     if geori > max_distance:
#         max_distance = geori
#         number = next
#     geori += 1
#     for next2 in road[next]:
#         if distance[next2] > geori:
#             distance[next2] = geori
#             heapq.heappush(heap, (geori, next2))
#
# print(number, max_distance, distance.count(max_distance))


# 다익스트라?
# import heapq
# N, M = map(int, input().split())
# road = [[] for _ in range(N+1)]
# # 1번 헛간에서의 거리
# distance = [50000] * (N+1)
#
# for _ in range(M):
#     start, end = map(int, input().split())
#     road[start].append(end)
#     road[end].append(start)
#
# heap = [(0, 1)]
# distance[1] = 0
#
# while heap:
#     geori, next = heapq.heappop(heap)
#     if geori <= distance[next]:
#         geori += 1
#         for next2 in road[next]:
#             if distance[next2] > geori:
#                 distance[next2] = geori
#                 heapq.heappush(heap, (geori, next2))
#
# max_distance = number = cnt = 0
# for i in range(2, N+1):
#     if distance[i] > max_distance:
#         cnt = 1
#         max_distance = distance[i]
#         number = i
#     elif distance[i] == max_distance:
#         cnt += 1
#
# print(number, max_distance, cnt)

# 함수로
# import heapq
# N, M = map(int, input().split())
# road = [[] for _ in range(N+1)]
# # 1번 헛간에서의 거리
# distance = [50000] * (N+1)
#
# for _ in range(M):
#     start, end = map(int, input().split())
#     road[start].append(end)
#     road[end].append(start)
#
#
# def dijkstra():
#     heap = [(0, 1)]
#     distance[1] = 0
#     while heap:
#         geori, next = heapq.heappop(heap)
#         if geori <= distance[next]:
#             geori += 1
#             for next2 in road[next]:
#                 if distance[next2] > geori:
#                     distance[next2] = geori
#                     heapq.heappush(heap, (geori, next2))
#
#     max_distance = number = cnt = 0
#     for i in range(2, N+1):
#         if distance[i] > max_distance:
#             cnt = 1
#             max_distance = distance[i]
#             number = i
#         elif distance[i] == max_distance:
#             cnt += 1
#     return [number, max_distance, cnt]
#
# print(*dijkstra())



# 다익스트라?2
# import heapq
# N, M = map(int, input().split())
# road = [[] for _ in range(N+1)]
# # 1번 헛간에서의 거리
# distance = [0] * (N+1)
#
# for _ in range(M):
#     start, end = map(int, input().split())
#     road[start].append(end)
#     road[end].append(start)
#
# heap = [(0, 1)]
# distance[1] = 0
#
# while heap:
#     geori, next = heapq.heappop(heap)
#     if geori <= distance[next]:
#         geori += 1
#         for next2 in road[next]:
#             if distance[next2] == 0:
#                 distance[next2] = geori
#                 heapq.heappush(heap, (geori, next2))
#
# max_distance = number = cnt = 0
# for i in range(2, N+1):
#     if distance[i] > max_distance:
#         cnt = 1
#         max_distance = distance[i]
#         number = i
#     elif distance[i] == max_distance:
#         cnt += 1
#
# print(number, max_distance, cnt)
