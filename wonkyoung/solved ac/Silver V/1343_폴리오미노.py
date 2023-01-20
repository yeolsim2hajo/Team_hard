#230120
# 틀림
# board = input()
# x_cnt = 0
# result_board = ''
# for area in board:
#     if area == 'X':
#         x_cnt += 1
#     else:
#         if x_cnt % 2:
#             print(-1)
#             break
#         elif x_cnt:
#             result_board += 'A' * (x_cnt // 4 * 4) + 'B' * (x_cnt % 4)
#         result_board += '.'
#         x_cnt = 0
# else:
#     if x_cnt % 2:
#         print(-1)
#     elif x_cnt:
#         result_board += 'A'* (x_cnt//4 * 4) + 'B' * (x_cnt % 4)
#     print(result_board)

# 수정
# board = input()
# x_cnt = 0
# result_board = ''
# for area in board:
#     if area == 'X':
#         x_cnt += 1
#     else:
#         if x_cnt % 2:
#             print(-1)
#             break
#         elif x_cnt:
#             remain = x_cnt % 4
#             result_board += 'A' * (x_cnt - remain) + 'B' * remain
#         result_board += '.'
#         x_cnt = 0
# else:
#     if x_cnt % 2:
#         print(-1)
#     else:
#         if x_cnt:
#             result_board += 'A'* (x_cnt//4 * 4) + 'B' * (x_cnt % 4)
#         print(result_board)


# 함수화
# def change_board(board):
#     x_cnt = 0
#     result_board = ''
#     for area in board:
#         if area == 'X':
#             x_cnt += 1
#         else:
#             if x_cnt % 2:
#                 return -1
#             elif x_cnt:
#                 remain = x_cnt % 4
#                 result_board += 'A' * (x_cnt - remain) + 'B' * remain
#             result_board += '.'
#             x_cnt = 0
#     if x_cnt % 2:
#         return -1
#     if x_cnt:
#         result_board += 'A' * (x_cnt // 4 * 4) + 'B' * (x_cnt % 4)
#     return result_board
#
# board = input()
# print(change_board(board))


# 인자 X
# def change_board():
#     x_cnt = 0
#     result_board = ''
#     for area in board:
#         if area == 'X':
#             x_cnt += 1
#         else:
#             if x_cnt % 2:
#                 return -1
#             elif x_cnt:
#                 remain = x_cnt % 4
#                 result_board += 'A' * (x_cnt - remain) + 'B' * remain
#             result_board += '.'
#             x_cnt = 0
#     if x_cnt % 2:
#         return -1
#     if x_cnt:
#         result_board += 'A' * (x_cnt // 4 * 4) + 'B' * (x_cnt % 4)
#     return result_board
# board = input()
# print(change_board())


# . 앞으로
def change_board():
    x_cnt = 0
    result_board = ''
    for area in board:
        if area == 'X':
            x_cnt += 1
        elif x_cnt == 0:
            result_board += '.'
        elif x_cnt % 2:
            return -1
        else:
            remain = x_cnt % 4
            result_board += 'A' * (x_cnt - remain) + 'B' * remain + '.'
            x_cnt = 0
    if x_cnt % 2:
        return -1
    if x_cnt:
        result_board += 'A' * (x_cnt // 4 * 4) + 'B' * (x_cnt % 4)
    return result_board
board = input()
print(change_board())