#220620
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