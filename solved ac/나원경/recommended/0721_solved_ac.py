#3085 사탕 게임
# N = int(input())
# board = [list(map(str, input())) for _ in range(N)]
# max_candy = cnt = 1
#
# def update_cnt():
#     global max_candy, cnt
#     if max_candy < cnt:
#         max_candy = cnt
#     cnt = 1
# def count_horizontal(start=0, end=N):
#     global max_candy, cnt
#     for row in range(start, end):
#         cnt = 1
#         for col in range(N-1):
#             if board[row][col] == board[row][col+1]:
#                 cnt += 1
#             else:
#                 update_cnt()
#         update_cnt()
# def count_vertical(start=0, end=N):
#     global max_candy, cnt
#     for col in range(start, end):
#         cnt = 1
#         for row in range(N-1):
#             if board[row][col] == board[row+1][col]:
#                 cnt += 1
#             else:
#                 update_cnt()
#         update_cnt()
#
# def exchange_candy():
#     for i in range(N):
#         for j in range(N-1):
#             if board[i][j] != board[i][j + 1]:
#                 board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
#                 count_horizontal(i, i + 1)
#                 count_vertical(j, j+2)
#                 board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
#     for j in range(N):
#         for i in range(N-1):
#             if board[i][j] != board[i+1][j]:
#                 board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
#                 count_horizontal(i, i+2)
#                 count_vertical(j, j+1)
#                 board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
#
# count_horizontal()
# if max_candy != N:
#     exchange_candy()
# print(max_candy)



# 틀림 - 다시
# N = int(input())
# board = [list(map(str, input())) for _ in range(N)]
# rot_board = board[:]
# max_candy = cnt = 1
# def rotate():
#     for i in range(N):
#         for j in range(N):
#             if i > j:
#                 rot_board[i][j], rot_board[j][i] = rot_board[j][i], rot_board[i][j]
# rotate()
#
# def update_cnt():
#     global max_candy, cnt
#     if max_candy < cnt:
#         max_candy = cnt
#     cnt = 1
# def count_candy(lst, start=0, end=N):
#     global cnt
#     for row in range(start, end):
#         for col in range(N-1):
#             if lst[row][col] == lst[row][col+1]:
#                 cnt += 1
#             else:
#                 update_cnt()
#         update_cnt()
#
# def exchange_candy(lst1, lst2):
#     for i in range(N):
#         for j in range(N-1):
#             if lst1[i][j] != lst1[i][j + 1]:
#                 lst1[i][j], lst1[i][j + 1] = lst1[i][j + 1], lst1[i][j]
#                 lst2[j][i], lst2[j+1][i] = lst2[j+1][i], lst2[j][i]
#                 count_candy(lst1, i, i + 1)
#                 count_candy(lst2, j, j+2)
#                 lst1[i][j], lst1[i][j + 1] = lst1[i][j + 1], lst1[i][j]
#                 lst2[j][i], lst2[j+1][i] = lst2[j+1][i], lst2[j][i]
#
# count_candy(board)
# count_candy(rot_board)
# if max_candy != N:
#     exchange_candy(board, rot_board)
#     exchange_candy(rot_board, board)
# print(max_candy)