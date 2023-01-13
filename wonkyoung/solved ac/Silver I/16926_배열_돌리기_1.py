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


#230113
# period 변경 - 시간 덜 걸림
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
#             cnt = R % period if period > 0 else 0
#             for cnt in range(cnt):
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
#     period -= 8
#
# for i in range(N):
#     print(' '.join(new_arr[i]))


# 틀림
# import sys
# new_input = sys.stdin.readline
# N, M, R = map(int, new_input().split())
# arr = [new_input().split() for _ in range(N)]
# limit = N//2 if N <= M else M//2
# new_arr = [[0]*M for _ in range(N)]
# period = 2*(N+M-2)
# def change_arr():
#     temp_arr = []
#     last_row, last_col = N-1-i, M-1-i
#     for k in range(i, last_row):
#         temp_arr.append((k, i))
#     for k in range(i, last_col):
#         temp_arr.append((last_row, k))
#     for k in range(last_row, i, -1):
#         temp_arr.append((k, last_col))
#     for k in range(last_col, i, -1):
#         temp_arr.append((i, k))
#     cnt = R%period if period else 0
#     for _ in range(cnt):
#         temp_arr = temp_arr[-1:] + temp_arr[:-1]
#
#     index = 0
#     for k in range(i, last_row):
#         y, x = temp_arr[index]
#         new_arr[k][i] = arr[y][x]
#         index += 1
#     for k in range(i, last_col):
#         y, x = temp_arr[index]
#         new_arr[last_row][k] = arr[y][x]
#         index += 1
#     for k in range(last_row, i, -1):
#         y, x = temp_arr[index]
#         new_arr[k][last_col] = arr[y][x]
#         index += 1
#     for k in range(last_col, i, -1):
#         y, x = temp_arr[index]
#         new_arr[i][k] = arr[y][x]
#         index += 1
#
# for i in range(limit):
#     change_arr()
#     period -= 2
#
# for i in range(N):
#     print(' '.join(new_arr[i]))



# 1차원
# import sys
# new_input = sys.stdin.readline
# N, M, R = map(int, new_input().split())
# arr = [new_input().split() for _ in range(N)]
# limit = N//2 if N <= M else M//2
# new_arr = [[0]*M for _ in range(N)]
# period = 2*(N+M-2)
# def change_arr():
#     temp_arr = []
#     last_row, last_col = N-1-i, M-1-i
#     for k in range(i, last_row):
#         temp_arr.append(arr[k][i])
#     for k in range(i, last_col):
#         temp_arr.append(arr[last_row][k])
#     for k in range(last_row, i, -1):
#         temp_arr.append(arr[k][last_col])
#     for k in range(last_col, i, -1):
#         temp_arr.append(arr[i][k])
#     cnt = R%period if period else 0
#     for _ in range(cnt):
#         temp_arr = temp_arr[-1:] + temp_arr[:-1]
#
#     index = 0
#     for k in range(i, last_row):
#         new_arr[k][i] = temp_arr[index]
#         index += 1
#     for k in range(i, last_col):
#         new_arr[last_row][k] = temp_arr[index]
#         index += 1
#     for k in range(last_row, i, -1):
#         new_arr[k][last_col] = temp_arr[index]
#         index += 1
#     for k in range(last_col, i, -1):
#         new_arr[i][k] = temp_arr[index]
#         index += 1
#
# for i in range(limit):
#     change_arr()
#     period -= 8
#
# for i in range(N):
#     print(' '.join(new_arr[i]))



# 깔끔하게 정리
# import sys
# new_input = sys.stdin.readline
# N, M, R = map(int, new_input().split())
# arr = [new_input().split() for _ in range(N)]
# limit = N//2 if N <= M else M//2
# new_arr = [[0]*M for _ in range(N)]
# period = 2*(N+M-2)
# def change_arr():
#     temp_arr = []
#     last_row, last_col = N-1-i, M-1-i
#     rotate_list = [(i, last_row, 1, i),
#                    (i, last_col, 1, last_row),
#                    (last_row, i, -1, last_col),
#                    (last_col, i, -1, i)]
#
#     rotate = 0
#     for start, end, step, const in rotate_list:
#         if rotate%2:
#             for k in range(start, end, step):
#                 temp_arr.append(arr[const][k])
#         else:
#             for k in range(start, end, step):
#                 temp_arr.append(arr[k][const])
#         rotate += 1
#
#     cnt = R%period if period else 0
#     for _ in range(cnt):
#         temp_arr = temp_arr[-1:] + temp_arr[:-1]
#     index = rotate = 0
#     for start, end, step, const in rotate_list:
#         if rotate%2:
#             for k in range(start, end, step):
#                 new_arr[const][k] = temp_arr[index]
#                 index += 1
#         else:
#             for k in range(start, end, step):
#                 new_arr[k][const] = temp_arr[index]
#                 index += 1
#         rotate += 1
#
# for i in range(limit):
#     change_arr()
#     period -= 8
#
# for i in range(N):
#     print(' '.join(new_arr[i]))

'''
4 4 2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''

'''
5 4 7
1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 28
'''

# 함수화
# import sys
# new_input = sys.stdin.readline
# N, M, R = map(int, new_input().split())
# arr = [new_input().split() for _ in range(N)]
# limit = N//2 if N <= M else M//2
# new_arr = [[0]*M for _ in range(N)]
# period = 2*(N+M-2)
#
# def change_arr():
#     temp_arr = []
#     last_row, last_col = N-1-i, M-1-i
#     rotate_list = [(i, last_row, 1, i),
#                    (i, last_col, 1, last_row),
#                    (last_row, i, -1, last_col),
#                    (last_col, i, -1, i)]
#
#     def fill_arr(option):
#         if option == 'temp_arr':
#             rotate = 0
#             def one_func():
#                 temp_arr.append(arr[const][k])
#             def zero_func():
#                 temp_arr.append(arr[k][const])
#             def rotate_arr():
#                 nonlocal temp_arr
#                 cnt = R % period if period else 0
#                 for _ in range(cnt):
#                     temp_arr = temp_arr[-1:] + temp_arr[:-1]
#         else:
#             rotate = index = 0
#             def one_func():
#                 nonlocal index
#                 new_arr[const][k] = temp_arr[index]
#                 index += 1
#             def zero_func():
#                 nonlocal index
#                 new_arr[k][const] = temp_arr[index]
#                 index += 1
#
#         for start, end, step, const in rotate_list:
#             if rotate%2:
#                 for k in range(start, end, step):
#                     one_func()
#             else:
#                 for k in range(start, end, step):
#                     zero_func()
#             rotate += 1
#
#         if option == 'temp_arr':
#             rotate_arr()
#
#     fill_arr('temp_arr')
#     fill_arr('new_arr')
#
# for i in range(limit):
#     change_arr()
#     period -= 8
#
# for i in range(N):
#     print(' '.join(new_arr[i]))



# 더 깔끔 정리
# def change_arr():
#     temp_arr = []
#     last_row, last_col = N-1-i, M-1-i
#     rotate_list = [(i, last_row, 1, i),
#                    (i, last_col, 1, last_row),
#                    (last_row, i, -1, last_col),
#                    (last_col, i, -1, i)]
#
#     def fill_arr(option):
#         if option == 'temp_arr':
#             rotate = 0
#             def one_func():
#                 temp_arr.append(arr[const][k])
#             def zero_func():
#                 temp_arr.append(arr[k][const])
#             def rotate_arr():
#                 nonlocal temp_arr
#                 cnt = R % period if period else 0
#                 for _ in range(cnt):
#                     temp_arr = temp_arr[-1:] + temp_arr[:-1]
#         else:
#             rotate = index = 0
#             def one_func():
#                 nonlocal index
#                 new_arr[const][k] = temp_arr[index]
#                 index += 1
#             def zero_func():
#                 nonlocal index
#                 new_arr[k][const] = temp_arr[index]
#                 index += 1
#
#         for start, end, step, const in rotate_list:
#             if rotate%2:
#                 for k in range(start, end, step):
#                     one_func()
#             else:
#                 for k in range(start, end, step):
#                     zero_func()
#             rotate += 1
#
#         if option == 'temp_arr':
#             rotate_arr()
#
#     fill_arr('temp_arr')
#     fill_arr('new_arr')
#
# import sys
# new_input = sys.stdin.readline
# N, M, R = map(int, new_input().split())
# arr = [new_input().split() for _ in range(N)]
# limit = min(N, M)//2
# new_arr = [[0]*M for _ in range(N)]
# period = 2*(N+M-2)
#
# for i in range(limit):
#     change_arr()
#     period -= 8
#
# for i in range(N):
#     print(' '.join(new_arr[i]))


# pop, insert 사용
# def change_arr():
#     temp_arr = []
#     last_row, last_col = N-1-i, M-1-i
#     rotate_list = [(i, last_row, 1, i),
#                    (i, last_col, 1, last_row),
#                    (last_row, i, -1, last_col),
#                    (last_col, i, -1, i)]
#
#     def fill_arr(option):
#         if option == 'temp_arr':
#             rotate = 0
#             def one_func():
#                 temp_arr.append(arr[const][k])
#             def zero_func():
#                 temp_arr.append(arr[k][const])
#             def rotate_arr():
#                 nonlocal temp_arr
#                 cnt = R % period if period else 0
#                 for _ in range(cnt):
#                     last = temp_arr.pop()
#                     temp_arr.insert(0, last)
#         else:
#             rotate = index = 0
#             def one_func():
#                 nonlocal index
#                 new_arr[const][k] = temp_arr[index]
#                 index += 1
#             def zero_func():
#                 nonlocal index
#                 new_arr[k][const] = temp_arr[index]
#                 index += 1
#
#         for start, end, step, const in rotate_list:
#             if rotate%2:
#                 for k in range(start, end, step):
#                     one_func()
#             else:
#                 for k in range(start, end, step):
#                     zero_func()
#             rotate += 1
#
#         if option == 'temp_arr':
#             rotate_arr()
#
#     fill_arr('temp_arr')
#     fill_arr('new_arr')
#
# import sys
# new_input = sys.stdin.readline
# N, M, R = map(int, new_input().split())
# arr = [new_input().split() for _ in range(N)]
# limit = min(N, M)//2
# new_arr = [[0]*M for _ in range(N)]
# period = 2*(N+M-2)
#
# for i in range(limit):
#     change_arr()
#     period -= 8
#
# for i in range(N):
#     print(' '.join(new_arr[i]))

# deque 사용 - 시간 더 걸림
def change_arr():
    from collections import deque
    temp_arr = deque()
    last_row, last_col = N-1-i, M-1-i
    rotate_list = [(i, last_row, 1, i),
                   (i, last_col, 1, last_row),
                   (last_row, i, -1, last_col),
                   (last_col, i, -1, i)]

    def fill_arr(option):
        if option == 'temp_arr':
            rotate = 0
            def one_func():
                temp_arr.append(arr[const][k])
            def zero_func():
                temp_arr.append(arr[k][const])
            def rotate_arr():
                nonlocal temp_arr
                cnt = R % period if period else 0
                for _ in range(cnt):
                    last = temp_arr.pop()
                    temp_arr.appendleft(last)
        else:
            rotate = index = 0
            def one_func():
                nonlocal index
                new_arr[const][k] = temp_arr[index]
                index += 1
            def zero_func():
                nonlocal index
                new_arr[k][const] = temp_arr[index]
                index += 1

        for start, end, step, const in rotate_list:
            if rotate%2:
                for k in range(start, end, step):
                    one_func()
            else:
                for k in range(start, end, step):
                    zero_func()
            rotate += 1

        if option == 'temp_arr':
            rotate_arr()

    fill_arr('temp_arr')
    fill_arr('new_arr')

import sys
new_input = sys.stdin.readline
N, M, R = map(int, new_input().split())
arr = [new_input().split() for _ in range(N)]
limit = min(N, M)//2
new_arr = [[0]*M for _ in range(N)]
period = 2*(N+M-2)

for i in range(limit):
    change_arr()
    period -= 8

for i in range(N):
    print(' '.join(new_arr[i]))