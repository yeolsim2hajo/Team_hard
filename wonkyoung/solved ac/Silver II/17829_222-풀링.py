#221219
# number = int(input())
# matrix = [list(map(int, input().split())) for _ in range(number)]
# while number > 1:
#     number //= 2
#     new_matrix = [[0] * number for _ in range(number)]
#     for i in range(0, number):
#         for j in range(0, number):
#             first_max = second_max = -1e4
#             for di in range(2):
#                 ni = 2*i+di
#                 for dj in range(2):
#                     nj = 2*j+dj
#                     element = matrix[ni][nj]
#                     if element > first_max:
#                         first_max, second_max = element, first_max
#                     elif element > second_max:
#                         second_max = element
#             new_matrix[i][j] = second_max
#     matrix = [new_matrix[i] for i in range(number)]
# print(matrix[0][0])


# 함수형
# def pooling(number):
#     matrix = [list(map(int, new_input().split())) for _ in range(N)]
#     while number > 1:
#         number //= 2
#         new_matrix = [[0] * number for _ in range(number)]
#         for i in range(0, number):
#             for j in range(0, number):
#                 first_max = second_max = -1e4
#                 for di in range(2):
#                     ni = 2*i+di
#                     for dj in range(2):
#                         nj = 2*j+dj
#                         element = matrix[ni][nj]
#                         if element > first_max:
#                             first_max, second_max = element, first_max
#                         elif element > second_max:
#                             second_max = element
#                 new_matrix[i][j] = second_max
#         matrix = [new_matrix[i] for i in range(number)]
#     return matrix[0][0]
#
# import sys
# new_input = sys.stdin.readline
# N = int(new_input())
# print(pooling(N))



# 함수 2
def pooling(number):

    matrix = [list(map(int, new_input().split())) for _ in range(N)]
    def find_second_max(row, col):
        first_max = second_max = -1e4
        for dr in range(2):
            nr = row + dr
            for dc in range(2):
                nc = col + dc
                element = matrix[nr][nc]
                if element > first_max:
                    first_max, second_max = element, first_max
                elif element > second_max:
                    second_max = element
        return second_max

    while number > 1:
        number //= 2
        new_matrix = [[0] * number for _ in range(number)]
        for i in range(0, number):
            for j in range(0, number):
                new_matrix[i][j] = find_second_max(2*i, 2*j)
        matrix = [new_matrix[i] for i in range(number)]
    return matrix[0][0]

import sys
new_input = sys.stdin.readline
N = int(new_input())
print(pooling(N))

