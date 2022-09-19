#16956 늑대와 양
# import sys
# new_input = sys.stdin.readline
# R, C = map(int, new_input().split())
# farm, sheep, wolves = [], [], []
# path, visited = set(), set()
# for i in range(R):
#     farm.append(list(map(str, new_input().rstrip())))
#     for j in range(C):
#         if farm[i][j] == 'S':
#             sheep.append((i,j))
#         elif farm[i][j] == 'W':
#             wolves.append((i,j))
# for y,x in wolves:
#     temp = sheep[:]
#     while temp:
#         dest_y, dest_x = temp.pop(0)
#         for dy, dx in (-1,0), (1,0), (0,-1), (0,1):
#             ny, nx = y+dy, x+dx
#             if 0 <= ny < R and 0 <= nx < C:
#                 if (ny, nx) not in visited:
#                     path.add((ny, nx))
#                     visited.add((ny, nx))
#
# for _ in range(R):
#     print(*farm)


#1926 그림
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# picture = set()
# def find_picture():
#     for i in range(N):
#         row = new_input().split()
#         for j in range(M):
#             if row[j] == '1':
#                 picture.add((i,j))
# def calc_picture():
#     from collections import deque
#     cnt = max_size = 0
#     while picture:
#         y, x = picture.pop()
#         cnt += 1
#         size = 1
#         q = deque([(y,x)])
#         while q:
#             ny, nx = q.pop()
#             for dy, dx in (-1,0), (1,0), (0,-1), (0,1):
#                 move = (ny+dy, nx+dx)
#                 if move in picture:
#                     picture.remove(move)
#                     q.append(move)
#                     size += 1
#         max_size = max(size, max_size)
#     print(cnt, max_size, sep='\n')
#
# find_picture()
# calc_picture()

# 시간 더 걸림
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# picture = set()
# def find_picture():
#     for i in range(N):
#         row = new_input().split()
#         for j in range(M):
#             if row[j] == '1':
#                 picture.add((i,j))
# def calc_picture():
#     from collections import deque
#     cnt = max_size = 0
#     while picture:
#         cnt += 1
#         size = 1
#         q = deque([picture.pop()])
#         while q:
#             ny, nx = q.pop()
#             for dy, dx in (-1,0), (1,0), (0,-1), (0,1):
#                 move = (ny+dy, nx+dx)
#                 if move in picture:
#                     picture.remove(move)
#                     q.append(move)
#                     size += 1
#         max_size = max(size, max_size)
#     print(cnt, max_size, sep='\n')
#
# find_picture()
# calc_picture()
