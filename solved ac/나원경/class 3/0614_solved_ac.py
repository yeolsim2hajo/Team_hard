#9375 패션왕 신해빈 - 50%
# import sys
# T = int(input())
# def dfs(max_lev, start=0, lev=0):
#     global max_cnt
#     if lev == max_lev:
#         max_cnt += 1
#         return
#     for j in range(start,n):
#         if clothes[j] not in path:
#             path.add(clothes[j])
#             dfs(max_lev, j, lev+1)
#             path.remove(clothes[j])
# new_input = sys.stdin.readline
# for _ in range(T):
#     clothes = []
#     n = int(new_input())
#     for _ in range(n):
#         data = new_input().split()
#         clothes.append(data[1])
#     path = set()
#     max_cnt = 0
#     limit = len(set(clothes))
#     for i in range(1,limit+1):
#         dfs(i)
#     print(max_cnt)


#9461 파도반 수열
# T = int(input())
# numbers = []
# for _ in range(T):
#     N = int(input())
#     if len(numbers) >= N:
#         print(numbers[N-1])
#     else:


#10026 적록색약
# N = int(input())
# picture = [input() for _ in range(N)]
# rg_same_cnt = cnt = 0
# visited = [[False] * N for _ in range(N)]
# def bfs(*args):
#     global cnt
#     q = [args]
#     new_q = [args]
#     color = picture[args[0]][args[1]]
#     while q:
#         y,x = q.pop(0)
#         for dy,dx in (-1,0), (1,0), (0,-1), (0,1):
#             ny, nx = y+dy, x+dx
#             if 0 <= ny < N and 0 <= nx < N:
#                 if visited[ny][nx] is False and picture[ny][nx] == color:
#                     visited[ny][nx] = True
#                     q.append((ny,nx))
#                     if color != 'B':
#                         new_q.append((ny,nx))
#     while new_q:
#         y,x = new_q.pop(0)
#         for dy,dx in (-1,0), (1,0), (0,-1), (0,1):
#             ny, nx = y+dy, x+dx
#             if 0 <= ny < N and 0 <= nx < N:
#                 if visited[ny][nx] is False and picture[ny][nx] not in {color, 'B'}:
#                     new_q.append((ny,nx))
#
#
# for i in range(N):
#     for j in range(N):
#         if visited[i][j] is False:
#             rg_same_cnt += 1
#             cnt += 1
#             visited[i][j] = True
#             bfs(i,j)


#11047 동전 0
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
cnt = 0
for i in range(N-1, -1, -1):
    if K // coins[i]:
        mod, quot = divmod(K, coins[i])
        cnt += mod
        K = quot
    if K == 0:
        break
print(cnt)
