#2579 계단 오르기
# N = int(input())
# steps = [0]+[int(input()) for _ in range(N)]
# now = N-1
# total = steps[-1]
# cnt = 1
# while now:
#     if now == 1:
#         break
#     elif cnt == 1 and steps[now-1] >= steps[now-2]:
#         now -= 1
#         total += steps[now]
#         cnt += 1
#     else:
#         now -= 2
#         total += steps[now]
#         cnt = 1
# print(total)


#6064 카잉 달력
# T = int(input())
# for _ in range(T):
#     M, N, x, y = map(int,input().split())
#     if x == y:
#         number = x
#     else:
#         if N > M:
#             N, M = M, N
#             x, y = y, x
#         end = M * N
#         if M%2 == N%2 == 0:
#             start = N
#         else:
#             start = N if N%2 else N-1
#         for i in range(N, 1, -2):
#             if M%i == N%i == 0:
#                 end //= i
#                 break
#         number = M + x
#         while number <= end:
#             remain = number%N
#             if remain == y or (remain == 0 and y == N):
#                 break
#             number += M
#         else:
#             number = -1
#     print(number)


#7569 토마토
# set 이용 - 틀림 - 동시에 처리되어야 하는 게 안 돼서 값이 다르게 나오는 듯
# M, N, H = map(int,input().split())
# mature = set()
# immature = set()
# for k in range(H):
#     for i in range(N):
#         box = input().split()
#         for j in range(M):
#             if box[j] == '1':
#                 mature.add((k,i,j,0))
#             elif box[j] == '0':
#                 immature.add((k, i, j))
#
# day = 0
# if immature:
#     while mature:
#         z, y, x, cnt = mature.pop()
#         if cnt > day:
#             day = cnt
#         for dz, dy, dx in (1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1):
#             nz, ny, nx = z+dz, y+dy, x+dx
#             if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
#                 if (nz, ny, nx) in immature:
#                     immature.remove((nz, ny, nx))
#                     mature.add((nz, ny, nx, cnt+1))
#     if immature:
#         day = -1
# print(day)


# deque + set - 시간 초과 또는 틀림
# from collections import deque
# M, N, H = map(int,input().split())
# mature = deque()
# immature = set()
# for k in range(H):
#     for i in range(N):
#         box = input().split()
#         for j in range(M):
#             if box[j] == '1':
#                 mature.append((k,i,j,0))
#             elif box[j] == '0':
#                 immature.add((k, i, j))
#
# day = 0
# if immature:
#     while mature:
#         z, y, x, day = mature.popleft()
#         for dz, dy, dx in (1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1):
#             nz, ny, nx = z+dz, y+dy, x+dx
#             if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
#                 if (nz, ny, nx) in immature:
#                     immature.remove((nz, ny, nx))
#                     mature.append((nz, ny, nx, day+1))
#         if not immature:
#             day += 1
#             break
#     else:
#         day = -1
# print(day)


# break 없앰
# from collections import deque
# M, N, H = map(int,input().split())
# mature = deque()
# immature = set()
# for k in range(H):
#     for i in range(N):
#         box = input().split()
#         for j in range(M):
#             if box[j] == '1':
#                 mature.append((k,i,j,0))
#             elif box[j] == '0':
#                 immature.add((k, i, j))
#
# day = 0
# if immature:
#     while mature:
#         z, y, x, day = mature.popleft()
#         for dz, dy, dx in (1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1):
#             nz, ny, nx = z+dz, y+dy, x+dx
#             if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
#                 if (nz, ny, nx) in immature:
#                     immature.remove((nz, ny, nx))
#                     mature.append((nz, ny, nx, day+1))
#     if immature:
#         day = -1
# print(day)




# bfs - 부적절?
# from collections import deque
# M, N, H = map(int,input().split())
# boxs = []
# for _ in range(H):
#     boxs.append([input().split() for _ in range(N)])
#
# def bfs():
#     day = 0
#     mature = deque()
#     for k in range(H):
#         for i in range(N):
#             for j in range(M):
#                 if boxs[k][i][j] == '1':
#                     mature.append((k,i,j,0))
#
#     while mature:
#         z, y, x, cnt = mature.popleft()
#         for dz, dy, dx in (1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1):
#             nz, ny, nx = z+dz, y+dy, x+dx
#             if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
#                 if boxs[nz][ny][nx] == '0':
#                     boxs[nz][ny][nx] = '1'
#                     mature.append((nz, ny, nx, cnt+1))
#         if not immature:
#             return day
#     else:
#         return -1
# print(bfs())