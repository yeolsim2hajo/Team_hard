#1058 친구
# N = int(input())
# friends = [input() for _ in range(N)]
# people = [0]*N
# visited = [[False] * N for _ in range(N)]
# for via in range(N):
#     for i in range(N):
#         for j in range(N):
#             if i < j:
#                 if not visited[i][j]:
#                     if friends[i][j] == 'Y':
#                         people[i] += 1
#                         people[j] += 1
#                         visited[i][j] = True
#                     elif friends[i][via] == friends[via][j] == 'Y':
#                         people[i] += 1
#                         people[j] += 1
#                         visited[i][j] = True
# print(max(people))


#1389 케빈 베이컨의 6단계 법칙
# N, M = map(int,input().split())
# min_num = limit = int(1e9)
# friends = [[limit] * (N+1) for _ in range(N+1)]
# for _ in range(M):
#     a, b = map(int,input().split())
#     friends[a][b] = friends[b][a] = 1
# for i in range(N):
#     friends[i][i] = 0
# for via in range(1,N+1):
#     for i in range(1,N+1):
#         for j in range(1,N+1):
#             friends[i][j] = min(friends[i][j] ,friends[i][via] + friends[via][j])
#
# for i in range(1,N+1):
#     total = 0
#     for j in range(1, N + 1):
#         if friends[i][j] != limit:
#             total += friends[i][j]
#     if total < min_num:
#         min_num = total
#         people = i
#
# print(people)


#11581 구호물자
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



