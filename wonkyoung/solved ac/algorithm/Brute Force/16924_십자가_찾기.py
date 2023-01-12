#221003 틀림
# import sys
# N, M = map(int, input().split())
# new_input = sys.stdin.readline
# board = [new_input().rstrip() for _ in range(N)]
# check = [board[i][:] for i in range(N)]
# cross = []
#
# def find_star():
#     def find_cross():
#         for size in range(1, min(i + 1, j + 1, N - i, M - j)):
#             if board[i][j - size:j + size + 1] == '*' * (2 * size + 1):
#                 for k in range(i - size, i + size + 1):
#                     if board[k][j] != '*':
#                         break
#                 else:
#                     cross.append([i + 1, j + 1, size])
#
#     for i in range(1, N-1):
#         for j in range(1, M-1):
#             if board[i][j] == '*':
#                 find_cross()
# find_star()
# print(len(cross))
# for element in cross:
#     print(*element)


#221008 - 틀림 - 나중에 다시
# N, M = map(int, input().split())
# board = [['.'] * M]
# position, backup = set(), set()
# limit = (min(N, M) - 1) // 2
# center = []
#
# for i in range(1, N + 1):
#     row = ['.'] + list(map(str, input()))
#     for j in range(1, M + 1):
#         if row[j] == '*':
#             position.add((i, j))
#     board.append(row)
#
# backup.update(position)
#
# def discard_star(row, col, size):
#     if position:
#         position.discard((row, col))
#         for i in [row - size, row + size]:
#             position.discard((i, col))
#         for j in [col - size, col + size]:
#             position.discard((row, j))
#
# def find_star(row, col, size):
#     for i in [row-size, row+size]:
#         if i > N or board[i][col] == '.':
#             return False
#     for j in [col-size, col+size]:
#         if j > N or board[row][j] == '.':
#             return False
#     discard_star(row, col, size)
#     center.append([row, col, size])
#     return True
#
# for y, x in backup:
#     for size in range(1, limit+1):
#         if not find_star(y, x, size):
#             break
#
# if not position:
#     for element in center:
#         print(*element)
# else:
#     print(-1)


#221008
# list 요소 개수 안 들어가서 계속 틀린 듯 - 느림
# N, M = map(int, input().split())
# board = [['.'] * (M+1)]
# position, backup = set(), set()
# limit = (min(N, M) - 1) // 2
# center = []
#
# for i in range(1, N + 1):
#     row = ['.'] + list(map(str, input()))
#     for j in range(1, M + 1):
#         if row[j] == '*':
#             position.add((i, j))
#     board.append(row)
#
# backup.update(position)
#
# def discard_star(row, col, size):
#     if position:
#         position.discard((row, col))
#         for i in [row - size, row + size]:
#             position.discard((i, col))
#         for j in [col - size, col + size]:
#             position.discard((row, j))
#
# def find_star(row, col, size):
#     for i in [row-size, row+size]:
#         if i > N or board[i][col] == '.':
#             return False
#     for j in [col-size, col+size]:
#         if j > M or board[row][j] == '.':
#             return False
#     discard_star(row, col, size)
#     center.append([row, col, size])
#     return True
#
# for y, x in backup:
#     for size in range(1, limit+1):
#         if not find_star(y, x, size):
#             break
#
# if not position:
#     print(len(center))
#     for element in center:
#         print(*element)
# else:
#     print(-1)


#board 없애기 - 시간 더 걸림
# N, M = map(int, input().split())
# position = set()
# limit = (min(N, M) - 1) // 2
# center = []
#
# for i in range(1, N + 1):
#     row = ['.'] + list(map(str, input()))
#     for j in range(1, M + 1):
#         if row[j] == '*':
#             position.add((i, j))
#
# backup = set(position)
#
# def discard_star(row, col, size):
#     if position:
#         position.discard((row, col))
#         for i in [row - size, row + size]:
#             position.discard((i, col))
#         for j in [col - size, col + size]:
#             position.discard((row, j))
#
# def find_star(row, col, size):
#     for i in [row-size, row+size]:
#         if i > N or (i, col) not in backup:
#             return False
#     for j in [col-size, col+size]:
#         if j > M or (row, j) not in backup:
#             return False
#     discard_star(row, col, size)
#     center.append([row, col, size])
#     return True
#
# for y, x in backup:
#     for size in range(1, limit+1):
#         if not find_star(y, x, size):
#             break
#
# if not position:
#     print(len(center))
#     for element in center:
#         print(*element)
# else:
#     print(-1)


# 함수로
# def find_cross():
#     N, M = map(int, input().split())
#     board = [['.'] * (M+1)]
#     position, backup = set(), set()
#     limit = (min(N, M) - 1) // 2
#     center = []
#
#     for i in range(1, N + 1):
#         row = ['.'] + list(map(str, input()))
#         for j in range(1, M + 1):
#             if row[j] == '*':
#                 position.add((i, j))
#         board.append(row)
#
#     backup.update(position)
#
#     def discard_star(row, col, size):
#         if position:
#             position.discard((row, col))
#             for i in [row - size, row + size]:
#                 position.discard((i, col))
#             for j in [col - size, col + size]:
#                 position.discard((row, j))
#
#     def find_star(row, col, size):
#         for i in [row-size, row+size]:
#             if i > N or board[i][col] == '.':
#                 return False
#         for j in [col-size, col+size]:
#             if j > M or board[row][j] == '.':
#                 return False
#         discard_star(row, col, size)
#         center.append([row, col, size])
#         return True
#
#     for y, x in backup:
#         for size in range(1, limit+1):
#             if not find_star(y, x, size):
#                 break
#
#     if not position:
#         print(len(center))
#         for element in center:
#             print(*element)
#     else:
#         print(-1)
# find_cross()


# in 다음의 list 재사용
# def find_cross():
#     N, M = map(int, input().split())
#     board = [['.'] * (M+1)]
#     position, backup = set(), set()
#     limit = (min(N, M) - 1) // 2
#     center = []
#
#     for i in range(1, N + 1):
#         row = ['.'] + list(map(str, input()))
#         for j in range(1, M + 1):
#             if row[j] == '*':
#                 position.add((i, j))
#         board.append(row)
#
#     backup.update(position)
#
#     def discard_star(row, col):
#         if position:
#             position.discard((row, col))
#             for i in rows:
#                 position.discard((i, col))
#             for j in cols:
#                 position.discard((row, j))
#
#     def find_star(row, col, size):
#         for i in rows:
#             if i > N or board[i][col] == '.':
#                 return False
#         for j in cols:
#             if j > M or board[row][j] == '.':
#                 return False
#         discard_star(row, col)
#         center.append([row, col, size])
#         return True
#
#     for y, x in backup:
#         for size in range(1, limit+1):
#             rows = [y-size, y+size]
#             cols = [x-size, x+size]
#             if not find_star(y, x, size):
#                 break
#
#     if not position:
#         print(len(center))
#         for element in center:
#             print(*element)
#     else:
#         print(-1)
# find_cross()

