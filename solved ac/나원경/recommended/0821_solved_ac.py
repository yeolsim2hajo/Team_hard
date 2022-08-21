# import sys
# new_input = sys.stdin.readline
# N, M, R = map(int, new_input().split())
# limit = min(N,M)//2
# def find_number():
#     if N == M:
#         return R%(2*(N+M-2))
#     else:
#         number = 2*(N+M-2)
#         for i in range(1,limit//2):
#             new = N+M-2-2*i
#             for j in range(new-1, 1):
#                 if new%j == number%j:
#                     new //= j
#                     break
#             number *= new
#         return number
#
# min_rot = find_number()
# arr = [new_input().split() for _ in range(N)]
#
# def rotate():
#     global arr
#     result = [[0]*M for _ in range(N)]
#     for _ in range(min_rot):
#         for i in range(limit):
#             for row in {i, N-i-1}:
#                 edge = {i:1, N-i-1:-1}
#                 for col in range(i, M-i):
#                     if (row,col) in {(i,i), (N-i-1,M-i-1)}:
#                         result[row + edge[row]][col] = arr[row][col]
#                     else:
#                         result[row][col-edge[row]] = arr[row][col]
#             for col in {i, M-i-1}:
#                 edge = {i: 1, M-i-1: -1}
#                 for row in range(i,N-i):
#                     if row not in {i, N-i-1}:
#                         result[row+edge[col]][col] = arr[row][col]
#         arr = [result[i][:] for i in range(N)]
#     if min_rot:
#         return result
#     else:
#         return arr
# arr = rotate()
# for i in range(N):
#     print(*arr[i])

'''
4 4 12
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

5 4 14
1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 28
'''

# import sys
# new_input = sys.stdin.readline
# N, M, R = map(int, new_input().split())
# limit = min(N,M)//2
# arr = [new_input().split() for _ in range(N)]
#
# def rotate():
#     global arr
#     result = [arr[i][:] for i in range(N)]
#     min_rot = R%(2*(N+M-2))
#     for i in range(limit):
#         for _ in range(min_rot-8*i):
#             for row in {i, N-i-1}:
#                 edge = {i:1, N-i-1:-1}
#                 for col in range(i, M-i):
#                     if (row,col) in {(i,i), (N-i-1,M-i-1)}:
#                         result[row + edge[row]][col] = arr[row][col]
#                     else:
#                         result[row][col-edge[row]] = arr[row][col]
#             for col in {i, M-i-1}:
#                 edge = {i: 1, M-i-1: -1}
#                 for row in range(i,N-i):
#                     if row not in {i, N-i-1}:
#                         result[row+edge[col]][col] = arr[row][col]
#             arr = [result[i][:] for i in range(N)]
#     return result
# arr = rotate()
# for i in range(N):
#     print(*arr[i])


# import sys
# new_input = sys.stdin.readline
# N, M, R = map(int, new_input().split())
# limit = min(N,M)//2
# arr = [new_input().split() for _ in range(N)]
#
# def rotate():
#     global arr
#     result = [arr[i][:] for i in range(N)]
#     min_rot = R%(2*(N+M-2))
#     for i in range(limit):
#         for row in {i, N-i-1}:
#             edge = {i:1, N-i-1:-1}
#             for col in range(i, M-i):
#                 new_row, new_col = row, col
#                 for _ in range(min_rot-8*i):
#                     if (row,col) in {(i,i), (N-i-1,M-i-1)}:
#                         new_row += edge[row]
#                     else:
#                         new_col -= edge[row]
#                 result[new_row][new_col] = arr[row][col]
#         for col in {i, M-i-1}:
#             edge = {i: 1, M-i-1: -1}
#             for row in range(i,N-i):
#                 if row not in {i, N-i-1}:
#                     new_row, new_col = row, col
#                     for _ in range(min_rot - 8 * i):
#                         if (row, col) in {(i, i), (N - i - 1, M - i - 1)}:
#                             new_row += edge[col]
#                     result[new_row][col] = arr[row][col]
#             arr = [result[i][:] for i in range(N)]
#     return result
# arr = rotate()
# for i in range(N):
#     print(*arr[i])


import sys

new_input = sys.stdin.readline
T = int(new_input())
arr = [[10],[1], [6,2,4,8], [1,3,9,7],[6,4],[5],[6],[1,7,9,3],[6,8,4,2],[1,9]]
for _ in range(T):
    a, b = map(int, new_input().split())
    last = a%10
    length = len(arr[last])
    if length == 1:
        answer = arr[last][0]
    else:
        answer = arr[last][b%length]
    print(answer)