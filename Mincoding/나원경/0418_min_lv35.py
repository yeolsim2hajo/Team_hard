#3 연쇄폭탄
# def count_sec():
#     index = 0
#     end = 0
#     while index < N**2:
#         second,y,x = bomb[index]
#         if info[y][x]:
#             info[y][x] = 0
#             end = second
#             for dy,dx in (-1,0),(1,0),(0,-1),(0,1):
#                 ny, nx = y+dy, x+dx
#                 if 0 <= ny < N and 0 <= nx < N and info[ny][nx]:
#                     info[ny][nx] = 0
#         index += 1
#
#     print(f'{end}초')
#
# N = int(input())
# info = ['']*N
# bomb = [[] for _ in range(N**2)]
# for i in range(N):
#     info[i] = list(map(int,input().split()))
#     for j in range(N):
#         idx = info[i][j]
#         bomb[idx-1] = [idx,i,j]
# count_sec()