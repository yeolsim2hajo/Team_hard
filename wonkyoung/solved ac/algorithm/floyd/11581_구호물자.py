#220620
# N = int(input())
# road_data = [[999]* (N+1) for _ in range(N+1)]
# for i in range(1,N):
#     M = int(input())
#     link = list(map(int,input().split()))
#     for j in range(M):
#         road_data[i][link[j]] = 1
# visited = [False] * (N+1)
# visited[1] = True
# def is_cycle():
#     start = 1
#     for via in range(1,N):
#         if road_data[start][via] == 1:
#             start = via
#             visited[via] = True
#             while True:
#                 if not visited[via]:
#                     pass
#                 if via == N:
#                     break
#
#
#
#         return 0
# if is_cycle():
#     print('CYCLE')
# else:
#     print('NO CYCLE')



