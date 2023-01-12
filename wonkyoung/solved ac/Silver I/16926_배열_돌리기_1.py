#230111
# 입력 받기

#230112
# 시간초과
# import sys
# new_input = sys.stdin.readline
# N, M, R = map(int, input().split())
# arr = [input().split() for _ in range(N)]
# limit = N if N <= M else M
# period = 2*(N+M-2)
# new_arr = [[0]*M for _ in range(N)]
# def change_arr(j_limit, k_limit, option):
#     for j in (i, j_limit):
#         start = i if option == 0 else i+1
#         for k in range(start, k_limit):
#             if option == 0:
#                 row, col = j, k
#             else:
#                 row, col = k, j
#             for cnt in range(R%period):
#                 if row == i:
#                     if col != i:
#                         col -= 1
#                     else:
#                         row += 1
#                 elif row == N-1-i:
#                     if col != M-1-i:
#                         col += 1
#                     else:
#                         row -= 1
#                 elif col == i:
#                     if row != N-1-i:
#                         row += 1
#                     else:
#                         col += 1
#                 else:
#                     if row != i:
#                         row -= 1
#                     else:
#                         col -= 1
#             if option == 0:
#                 new_arr[row][col] = arr[j][k]
#             else:
#                 new_arr[row][col] = arr[k][j]
# for i in range(limit//2):
#     change_arr(N-1-i, M-i, 0)
#     change_arr(M-1-i, N-i, 1)
#
# for i in range(N):
#     print(' '.join(new_arr[i]))


#
import sys
new_input = sys.stdin.readline
N, M, R = map(int, new_input().split())
arr = [new_input().split() for _ in range(N)]
limit = N//2 if N <= M else M//2
new_arr = [[0]*M for _ in range(N)]
period = 2*(N+M-2)
def change_arr(j_limit, k_limit, option):
    for j in (i, j_limit):
        start = i if option == 0 else i+1
        for k in range(start, k_limit):
            if option == 0:
                row, col = j, k
            else:
                row, col = k, j
            cnt = R%period if period else 0
            for _ in range(cnt):
                if row == i:
                    if col != i:
                        col -= 1
                    else:
                        row += 1
                elif row == N-1-i:
                    if col != M-1-i:
                        col += 1
                    else:
                        row -= 1
                elif col == i:
                    if row != N-1-i:
                        row += 1
                    else:
                        col += 1
                else:
                    if row != i:
                        row -= 1
                    else:
                        col -= 1
            if option == 0:
                new_arr[row][col] = arr[j][k]
            else:
                new_arr[row][col] = arr[k][j]

for i in range(limit):
    change_arr(N-1-i, M-i, 0)
    change_arr(M-1-i, N-i, 1)
    period -= 2

for i in range(N):
    print(' '.join(new_arr[i]))
