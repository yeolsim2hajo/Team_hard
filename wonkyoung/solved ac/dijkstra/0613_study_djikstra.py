# 18352 특정 거리의 도시 찾기
# import heapq, sys
# N, M, K, X = map(int,input().split())
# city_link = [[] for _ in range(N+1)]
# new_input = sys.stdin.readline
# for _ in range(M):
#     start, end = map(int, new_input().split())
#     heapq.heappush(city_link[start], (1,end))
# answer = []
# if city_link[X]:
#     result = [3.1e6] * (N+1)
#     heap = [(0,X)]
#     while heap:
#         cnt, via = heapq.heappop(heap)
#         # print(cnt,via)
#         if cnt > min(result[via], K):
#             continue
#         for path, end in city_link[via]:
#             if cnt + path > K:
#                 continue
#             if cnt + path < result[end]:
#                 result[end] = cnt + path
#                 heapq.heappush(heap, (result[end],end))
#     # print(result)
#     for i in range(1,N+1):
#         if result[i] == K:
#             answer.append(i)
# if answer:
#     print(*answer, sep='\n')
# else:
#     print(-1)


#
# import heapq
# N, D = map(int,input().split())
# roads = [[] for _ in range(D+1)]
# for _ in range(N):
#     start, end, length = map(int,input().split())
#     heapq.heappush(roads[start],(end, length))
# min_path = D
# path = 0
# end = 0
# for i in range(D+1):
#     if roads[i]:
#         if roads[i][0] > D:
#             break
#         path += roads[i][1] + i - end
#         end = roads[i][0]



