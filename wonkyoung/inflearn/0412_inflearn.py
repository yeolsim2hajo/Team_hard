# def make():
#     global bat
#     possible = False
#     def find(y,x):
#         global bat
#         nonlocal possible
#         from collections import deque
#         q = deque()
#         q.append((y,x))
#         visited = [[False]*5 for _ in range(5)]
#         visited[y][x] = True
#         bat[y][x] = '#'
#         while q:
#             now_y,now_x = q.popleft()
#             for i in range(2):
#                 ny,nx = now_y+i,now_x+1-i
#                 if y <= ny < y+n and x <= nx < x+n:
#                     if visited[ny][nx] == False:
#                         if ground[ny][nx] == '1':
#                             return
#                         else:
#                             bat[ny][nx] = '#'
#                             q.append((ny,nx))
#         possible = True
#
#     for n in range(5,0,-1):
#         for i in range(6 - n):
#             for j in range(6 - n):
#                 if ground[i][j] == '0':
#                     find(i, j)
#                 if possible:
#                     return
#                 bat = [ground[i][:] for i in range(5)]
#
# ground = []
# bat = []
# for i in range(5):
#     ground.append(input('텃밭을 입력하세요 : ').split())
#     bat.append(ground[i][:])
# make()
# for i in range(5):
#     print(*bat[i])