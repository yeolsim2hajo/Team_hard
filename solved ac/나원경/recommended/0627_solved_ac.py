#2583 영역 구하기
# N, M, K = map(int, input().split())
# paper = [[1] * M for _ in range(N)]
# for _ in range(K):
#     bottom_x, bottom_y, top_x, top_y = map(int,input().split())
#     for i in range(N - top_y, N - bottom_y):
#         for j in range(bottom_x, top_x):
#             paper[i][j] = 0
# area = []
# def bfs(*args):
#     global paper, area
#     q = [args]
#     cnt = 1
#     while q:
#         y,x = q.pop(0)
#         for dy,dx in (-1,0), (1,0), (0,-1), (0,1):
#             ny,nx = y+dy,x+dx
#             if 0 <= ny < N and 0 <= nx < M and paper[ny][nx]:
#                 paper[ny][nx] = 0
#                 cnt += 1
#                 q.append((ny,nx))
#     area.append(cnt)
#
# for i in range(N):
#     for j in range(M):
#         if paper[i][j]:
#             paper[i][j] = 0
#             bfs(i,j)
# print(len(area))
# print(*sorted(area))




#16439 치킨치킨치킨
#
# N, M = map(int, input().split())
# preference = [list(map(int,input().split())) for _ in range(N)]
# max_val = 0
# path = []
# def dfs(arg=0):
#     global max_val
#     if arg == 3:
#         total = 0
#         for j in range(N):
#             temp = []
#             for idx in path:
#                 temp.append(preference[j][idx])
#             total += max(temp)
#         if max_val < total:
#             max_val = total
#         return
#     for i in range(M):
#         path.append(i)
#         dfs(arg+1)
#         path.pop()
# dfs()
# print(max_val)

# zip 이용
# N, M = map(int, input().split())
# preference = list(zip(*[list(map(int,input().split())) for _ in range(N)]))
# max_val = 0
# path = []
# def dfs(arg=0, start=0):
#     global max_val
#     if arg == 3:
#         total = 0
#         for j in range(N):
#             plus = 0
#             for i in range(3):
#                 if plus < path[i][j]:
#                     plus = path[i][j]
#             total += plus
#         if max_val < total:
#             max_val = total
#         return
#     for i in range(start, M):
#         path.append(preference[i])
#         dfs(arg+1, i+1)
#         path.pop()
# dfs()
# print(max_val)


#17069 파이프 옮기기2 - 못 품
# N = int(input())
# house = [input().split() for _ in range(N)]
# def bfs():
#     global house
#     cnt = 0
#     q = [(0,1,0)]
#     visited = [[False] * N for _ in range(N)]
#     position = [[(0,1),(1,1)], [(1,0),(1,1)], [(0,1),(1,0),(1,1)]]
#     while q:
#         y,x,direction = q.pop(0)
#         if y == x == N-1:
#             cnt += 1
#             continue
#         for dy,dx in position[direction]:
#             ny, nx = y+dy, x+dx
#             if ny < N and nx < N and house[ny][nx] == '0' and visited[ny][nx] is False:
#                 if dy == dx == 1:
#                     if x < N-1 and y < N-1 and house[y][x+1] == house[y+1][x] == '0':
#                         visited[ny][nx] = True
#                         q.append((ny,nx,2))
#                 elif dy == 0:
#                     visited[ny][nx] = True
#                     q.append((ny,nx,0))
#                 else:
#                     visited[ny][nx] = True
#                     q.append((ny,nx,1))
#     return cnt
#
# print(bfs())
