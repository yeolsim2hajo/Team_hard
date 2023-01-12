#220620
# 플로이드
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