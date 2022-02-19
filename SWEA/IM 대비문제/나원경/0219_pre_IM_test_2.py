# 숫자 배열 회전
# import sys
# sys.stdin = open("input (4).txt", "r")

# def rot_90(number,matrix):
#     result = [['']*number for _ in range(number)]
#     ret_y = [num for num in range(number)] * number
#     ret_x = []
#     for idx in range(number - 1, -1, -1):
#         ret_x += [idx]*number
#     for i in range(n**2):
#         y,x = i//number,i%number
#         result[ret_y[i]][ret_x[i]] = matrix[y][x]
#     return result
#
# def rot_180(number,matrix):
#     result = [['']*number for _ in range(number)]
#     ret_y = []
#     for idx in range(number - 1, -1, -1):
#         ret_y += [idx]*number
#     ret_x = [num for num in range(number-1,-1,-1)] * number
#     for i in range(n**2):
#         y,x = i//number,i%number
#         result[ret_y[i]][ret_x[i]] = matrix[y][x]
#     return result
#
# def rot_270(number, matrix):
#     result = [[''] * number for _ in range(number)]
#     ret_y = [num for num in range(number - 1, -1, -1)] * number
#     ret_x = []
#     for idx in range(number):
#         ret_x += [idx] * number
#     for i in range(n ** 2):
#         y, x = i // number, i % number
#         result[ret_y[i]][ret_x[i]] = matrix[y][x]
#     return result
#
# T = int(input())
# for tc in range(1,T+1):
#     n = int(input())
#     arr = [list(map(int,input().split())) for _ in range(n)]
#     print(f'#{tc}')
#     for i in range(n):
#         print(*rot_90(n,arr)[i],' ',*rot_180(n, arr)[i],' ',*rot_270(n, arr)[i],sep='')

# 숫자 배열 회전 - 다시
def rot(angle,matrix):
    number = len(matrix)
    result = [['']*number for _ in range(number)]
    if angle == 90:
        for i in range(n**2):
            y,x = i//number,i%number
            result[x][number-y-1] = matrix[y][x]
    elif angle == 180:
        for i in range(n**2):
            y,x = i//number,i%number
            result[number-y-1][number-x-1] = matrix[y][x]
    elif angle == 270:
        for i in range(n**2):
            y,x = i//number,i%number
            result[number-x-1][y] = matrix[y][x]
    return result

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    print(f'#{tc}')
    for i in range(n):
        print(*rot(90,arr)[i],' ',*rot(180, arr)[i],' ',*rot(270, arr)[i],sep='')




# 어디에 단어가 들어갈 수 있을까?
# import sys
# sys.stdin = open("input(6).txt", "r")
#
# T = int(input())
# for tc in range(1,T+1):
#     n,k = map(int, input().split())
#     puzzle = [list(map(int,input().split())) for _ in range(n)]
#     ans = 0
#     for i in range(n):
#         cnt = 0
#         for j in range(n):
#             if puzzle[i][j]:
#                 cnt += 1
#             else:cnt = 0
#             if cnt == k:
#                 if j == n-1:
#                     ans += 1
#                 elif puzzle[i][j+1] == 0:
#                     ans += 1
#
#     for i in range(n):
#         cnt = 0
#         for j in range(n):
#             if puzzle[j][i]:
#                 cnt += 1
#             else:cnt = 0
#             if cnt == k:
#                 if j == n - 1:
#                     ans += 1
#                 elif puzzle[j+1][i] == 0:
#                     ans += 1
#     print(f'#{tc} {ans}')
