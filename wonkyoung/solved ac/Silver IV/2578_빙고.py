#230220
#230221
# board = []
# position = [() for _ in range(26)]
# bingo_cnt = number_cnt = 0
# for i in range(5):
#     row = list(map(int, input().split()))
#     for j in range(5):
#         position[row[j]] = (i, j)
#     board.append(row)
#
# for i in range(5):
#     row = list(map(int, input().split()))
#     if number_cnt == 0:
#         cnt = 1
#         for num in row:
#             y, x = position[num]
#             board[y][x] = 0
#
#             if x+y == 4:
#                 for j in range(5):
#                     if board[j][4-j]:
#                         break
#                 else:
#                     bingo_cnt += 1
#
#             if x == y:
#                 for j in range(5):
#                     if board[j][j]:
#                         break
#                 else:
#                     bingo_cnt += 1
#
#             for j in range(5):
#                 if board[j][x]:
#                     break
#             else:
#                 bingo_cnt += 1
#
#             for j in range(5):
#                 if board[y][j]:
#                     break
#             else:
#                 bingo_cnt += 1
#
#             if bingo_cnt >= 3:
#                 number_cnt = 5*i + cnt
#                 break
#             cnt += 1
# print(number_cnt)


#
def speak_bingo():
    board = []
    position = [() for _ in range(26)]
    def fill_list():
        for i in range(5):
            row = list(map(int, input().split()))
            for j in range(5):
                position[row[j]] = (i, j)
            board.append(row)

    def find_number_cnt():
        bingo_cnt = number_cnt = 0

        def increase_bingo_cnt(y, x):
            nonlocal bingo_cnt
            for j in range(5):
                if board[j][x]:
                    break
            else:
                bingo_cnt += 1

            for j in range(5):
                if board[y][j]:
                    break
            else:
                bingo_cnt += 1

            if x + y == 4:
                for j in range(5):
                    if board[j][4 - j]:
                        break
                else:
                    bingo_cnt += 1

            if x == y:
                for j in range(5):
                    if board[j][j]:
                        break
                else:
                    bingo_cnt += 1

        for i in range(5):
            row = list(map(int, input().split()))
            if number_cnt == 0:
                cnt = 1
                for num in row:
                    y, x = position[num]
                    board[y][x] = 0
                    increase_bingo_cnt(y, x)
                    if bingo_cnt >= 3:
                        number_cnt = 5*i + cnt
                        break
                    cnt += 1
        return number_cnt

    fill_list()
    return find_number_cnt()
print(speak_bingo())