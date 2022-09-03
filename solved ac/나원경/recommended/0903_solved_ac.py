#1890 점프
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# cnt = 0
# possible = [[0]*N for _ in range(N)]
# possible[0][0] = 1
# for i in range(N):
#     for j in range(N):
#         if i == j == N-1:
#             break
#         jump = board[i][j]
#         if i+jump == j == N-1 or i == j+jump == N-1:
#             possible[N-1][N-1] += possible[i][j]
#         else:
#             if i+jump < N:
#                 possible[i+jump][j] += possible[i][j]
#             if j+jump < N:
#                 possible[i][j+jump] += possible[i][j]
# print(possible[N-1][N-1])


# 더 걸림
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# cnt = 0
# possible = [[0]*N for _ in range(N)]
# possible[0][0] = 1
# for i in range(N):
#     for j in range(N):
#         if i == j == N-1:
#             continue
#         jump = board[i][j]
#         if i+jump == j == N-1 or i == j+jump == N-1:
#             possible[N-1][N-1] += possible[i][j]
#         else:
#             if i+jump < N:
#                 possible[i+jump][j] += possible[i][j]
#             if j+jump < N:
#                 possible[i][j+jump] += possible[i][j]
# print(possible[N-1][N-1])


# 함수로 만들어
# def cnt_path():
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     possible = [[0]*N for _ in range(N)]
#     possible[0][0] = 1
#     for i in range(N):
#         for j in range(N):
#             if i == j == N-1:
#                 continue
#             jump = board[i][j]
#             if i+jump == j == N-1 or i == j+jump == N-1:
#                 possible[N-1][N-1] += possible[i][j]
#             else:
#                 if i+jump < N:
#                     possible[i+jump][j] += possible[i][j]
#                 if j+jump < N:
#                     possible[i][j+jump] += possible[i][j]
#     print(possible[N-1][N-1])
# cnt_path()


# return -> print 72ms / print() -> return 68ms
# def cnt_path():
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     possible = [[0]*N for _ in range(N)]
#     possible[0][0] = 1
#     for i in range(N):
#         for j in range(N):
#             if i == j == N-1:
#                 print(possible[N-1][N-1])
#                 return
#             jump = board[i][j]
#             if i+jump == j == N-1 or i == j+jump == N-1:
#                 possible[N-1][N-1] += possible[i][j]
#             else:
#                 if i+jump < N:
#                     possible[i+jump][j] += possible[i][j]
#                 if j+jump < N:
#                     possible[i][j+jump] += possible[i][j]
# cnt_path()

# for문 따로 빼기
# def cnt_path():
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     possible = [[0]*N for _ in range(N)]
#     possible[0][0] = 1
#     for i in range(N-1):
#         for j in range(N-1):
#             jump_row, jump_col = i+board[i][j], j+board[i][j]
#             if jump_row < N:
#                 possible[jump_row][j] += possible[i][j]
#             if jump_col < N:
#                 possible[i][jump_col] += possible[i][j]
#
#     for i in range(N-1):
#         jump_row, jump_col = i + board[i][N-1], i + board[N-1][i]
#         if jump_row < N-1:
#             possible[jump_row][N-1] += possible[i][N-1]
#         if jump_col < N-1:
#             possible[N-1][jump_col] += possible[N-1][i]
#
#     for i in range(N-1):
#         jump_row, jump_col = i + board[i][N - 1], i + board[N - 1][i]
#         if jump_row == N - 1:
#             possible[N - 1][N - 1] += possible[i][N-1]
#         if jump_col == N - 1:
#             possible[N - 1][N - 1] += possible[N - 1][i]
#
#     print(possible[N-1][N-1])
# cnt_path()



# def cnt_path():
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     possible = [[0]*N for _ in range(N)]
#     cnt = 0
#     possible[0][0] = 1
#     for i in range(N-1):
#         for j in range(N-1):
#             jump_row, jump_col = i+board[i][j], j+board[i][j]
#             if jump_row < N:
#                 possible[jump_row][j] += possible[i][j]
#             if jump_col < N:
#                 possible[i][jump_col] += possible[i][j]
#
#     for i in range(N-1):
#         jump_row, jump_col = i + board[i][N-1], i + board[N-1][i]
#         if jump_row < N-1:
#             possible[jump_row][N-1] += possible[i][N-1]
#         if jump_col < N-1:
#             possible[N-1][jump_col] += possible[N-1][i]
#
#     for i in range(N-1):
#         jump_row, jump_col = i + board[i][N - 1], i + board[N - 1][i]
#         if jump_row == N - 1:
#             cnt += possible[i][N-1]
#         if jump_col == N - 1:
#             cnt += possible[N - 1][i]
#
#     return cnt
# print(cnt_path())


# jump_row, jump_col - 시간 더 걸림
# def cnt_path():
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     possible = [[0]*N for _ in range(N)]
#     possible[0][0] = 1
#     for i in range(N):
#         for j in range(N):
#             if i == j == N-1:
#                 print(possible[N-1][N-1])
#                 return
#             jump_row, jump_col = i+board[i][j], j+board[i][j]
#             if jump_row == j == N-1 or i == jump_col == N-1:
#                 possible[N-1][N-1] += possible[i][j]
#             else:
#                 if jump_row < N:
#                     possible[jump_row][j] += possible[i][j]
#                 if jump_col < N:
#                     possible[i][jump_col] += possible[i][j]
# cnt_path()


#1025 제곱수 찾기
# from math import isqrt
# N, M = map(int, input().split())
# table = [input() for _ in range(N)]
# max_num = -1
# def is_square_num(num):
#     global max_num
#     num = int(num)
#     if max_num >= num:
#         return
#     root = isqrt(num)
#     if root ** 2 == num:
#         max_num = num
#
# def dfs(row, col, number ,level=0, row_dif=0, col_dif=0):
#     if level == 0:
#         for k in range(N):
#             for l in range(M):
#                 if k != row or l != col:
#                     new_num = number+table[k][l]
#                     is_square_num(new_num)
#                     dfs(k, l, new_num, level+1, k-row, l-col)
#     else:
#         new_row, new_col = row+row_dif, col+col_dif
#         if 0 <= new_row < N and 0 <= new_col < M:
#             new_num = number + table[new_row][new_col]
#             is_square_num(new_num)
#             dfs(new_row, new_col, new_num, level + 1, row_dif, col_dif)
#
# for i in range(N):
#     for j in range(M):
#         is_square_num(table[i][j])
#         dfs(i,j,table[i][j])
# print(max_num)


# level 증가 X
# from math import isqrt
# N, M = map(int, input().split())
# table = [input() for _ in range(N)]
# max_num = -1
# def is_square_num(num):
#     global max_num
#     num = int(num)
#     if max_num >= num:
#         return
#     root = isqrt(num)
#     if root ** 2 == num:
#         max_num = num
#
# def dfs(row, col, number ,level=0, row_dif=0, col_dif=0):
#     if level == 0:
#         for k in range(N):
#             for l in range(M):
#                 if k != row or l != col:
#                     new_num = number+table[k][l]
#                     is_square_num(new_num)
#                     dfs(k, l, new_num, level+1, k-row, l-col)
#     else:
#         new_row, new_col = row+row_dif, col+col_dif
#         if 0 <= new_row < N and 0 <= new_col < M:
#             new_num = number + table[new_row][new_col]
#             is_square_num(new_num)
#             dfs(new_row, new_col, new_num, level, row_dif, col_dif)
#
# for i in range(N):
#     for j in range(M):
#         is_square_num(table[i][j])
#         dfs(i,j,table[i][j])
# print(max_num)


# max 값 나중에 비교 (return문 X) - 시간 더 걸림
# from math import isqrt
# N, M = map(int, input().split())
# table = [input() for _ in range(N)]
# max_num = -1
# def is_square_num(num):
#     global max_num
#     num = int(num)
#     root = isqrt(num)
#     if root ** 2 == num:
#         max_num = max(num, max_num)
#
# def dfs(row, col, number ,level=0, row_dif=0, col_dif=0):
#     if level == 0:
#         for k in range(N):
#             for l in range(M):
#                 if k != row or l != col:
#                     new_num = number+table[k][l]
#                     is_square_num(new_num)
#                     dfs(k, l, new_num, level+1, k-row, l-col)
#     else:
#         new_row, new_col = row+row_dif, col+col_dif
#         if 0 <= new_row < N and 0 <= new_col < M:
#             new_num = number + table[new_row][new_col]
#             is_square_num(new_num)
#             dfs(new_row, new_col, new_num, level, row_dif, col_dif)
#
# for i in range(N):
#     for j in range(M):
#         is_square_num(table[i][j])
#         dfs(i,j,table[i][j])
# print(max_num)


# level 없앰 - 시간 더 걸림
# from math import isqrt
# N, M = map(int, input().split())
# table = [input() for _ in range(N)]
# max_num = -1
# def is_square_num(num):
#     global max_num
#     num = int(num)
#     if max_num >= num:
#         return
#     root = isqrt(num)
#     if root ** 2 == num:
#         max_num = num
#
# def dfs(row, col, number, row_dif=0, col_dif=0):
#     if row_dif == 0 and col_dif == 0:
#         for k in range(N):
#             for l in range(M):
#                 if k != row or l != col:
#                     new_num = number+table[k][l]
#                     is_square_num(new_num)
#                     dfs(k, l, new_num, k-row, l-col)
#     else:
#         new_row, new_col = row+row_dif, col+col_dif
#         if 0 <= new_row < N and 0 <= new_col < M:
#             new_num = number + table[new_row][new_col]
#             is_square_num(new_num)
#             dfs(new_row, new_col, new_num, row_dif, col_dif)
#
# for i in range(N):
#     for j in range(M):
#         is_square_num(table[i][j])
#         dfs(i,j,table[i][j])
# print(max_num)


# 함수 들어가기 전 if문 - 시간 더 걸림
# from math import isqrt
# N, M = map(int, input().split())
# table = [input() for _ in range(N)]
# max_num = -1
# def is_square_num(num):
#     global max_num
#     num = int(num)
#     root = isqrt(num)
#     if root ** 2 == num:
#         max_num = num
#
# def dfs(row, col, number ,level=0, row_dif=0, col_dif=0):
#     if level == 0:
#         for k in range(N):
#             for l in range(M):
#                 if k != row or l != col:
#                     new_num = number+table[k][l]
#                     if int(new_num) > max_num:
#                         is_square_num(new_num)
#                     dfs(k, l, new_num, level+1, k-row, l-col)
#     else:
#         new_row, new_col = row+row_dif, col+col_dif
#         if 0 <= new_row < N and 0 <= new_col < M:
#             new_num = number + table[new_row][new_col]
#             if int(new_num) > max_num:
#                 is_square_num(new_num)
#             dfs(new_row, new_col, new_num, level, row_dif, col_dif)
#
# for i in range(N):
#     for j in range(M):
#         table_num = table[i][j]
#         if int(table_num) > max_num:
#             is_square_num(table_num)
#         dfs(i,j,table_num)
# print(max_num)