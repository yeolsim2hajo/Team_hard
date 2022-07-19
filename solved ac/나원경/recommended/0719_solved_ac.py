#3085 사탕게임 - 다시
# N = int(input())
# board = [list(map(str, input())) for _ in range(N)]
# rotate_board = board[:]
# max_candy = 1
# def cnt_candy(lst, option=0):
#     global max_candy
#     for i in range(N):
#         cnt = 1
#         for j in range(N-1):
#             if lst[i][j + 1] == lst[i][j]:
#                 cnt += 1
#             else:
#                 if cnt > max_candy:
#                     max_candy = cnt
#                     if max_candy == N:
#                         return
#                 cnt = 1
#             if option == 0 and i > j:
#                 rotate_board[i][j], rotate_board[j][i] = rotate_board[j][i], rotate_board[i][j]
# cnt_candy(board)
# cnt_candy(rotate_board, 1)
# if max_candy < N:
#     def exchange_candy(lst):
#         def find_max(lst):
#             global max_candy
#             if lst[row][col + 1] != board[row][col]:
#                 lst[row][col + 1], lst[row][col] = lst[row][col + 1], lst[row][col]
#                 for x in range(2):
#                     cnt = 1
#                     for y in range(N-1):
#                         if lst[y][col+x] == lst[y+1][col+x]:
#                             cnt += 1
#                         else:
#                             if cnt > max_candy:
#                                 max_candy = cnt
#                                 if max_candy == N:
#                                     return
#                             cnt = 1
#                 lst[row][col + 1], lst[row][col] = lst[row][col + 1], lst[row][col]
#         find_max(lst)
#         for row in range(N):
#             for col in range(N-1):
#                 exchange_candy(board)
#                 exchange_candy(rotate_board)
# print(max_candy)


#3613 Java vs C++
# is_java = is_cpp = False
# variable = input()
# small = {chr(97+i) for i in range(26)}
# def change_type():
#     name = list(map(str, variable))
#     if is_java:
#         idx = 0
#         while idx < len(name):
#             if name[idx].isupper():
#                 name[idx] = name[idx].lower()
#                 name.insert(idx, '_')
#                 idx += 1
#             idx += 1
#         return ''.join(name)
#     else:
#         idx = 0
#         while idx < len(name):
#             if name[idx] == '_':
#                 name.pop(idx)
#                 name[idx] = name[idx].upper()
#             idx += 1
#         return ''.join(name)
# if '_' in variable:
#     for alp in variable:
#         if alp != '_' and alp not in small:
#             break
#     else:
#         is_cpp = True
# else:
#     for alp in variable:
#         if alp.lower() not in small:
#             break
#     else:
#         is_java = True
# if is_java or is_cpp:
#     print(change_type())
# else:
#     print('Error!')





# 틀림
# variable = input()
# small = {chr(97+i) for i in range(26)}
# def change_type():
#     global type
#     if '_' in variable and variable[0] != '_' != variable[-1]:
#         for alp in variable:
#             if alp != '_' and alp not in small:
#                 return 'Error!'
#         name = variable.split('_')
#         for i in range(len(name)):
#             name[i][0] = name[i][0].capitalize()
#         return ''.join(name)
#
#     else:
#         if variable[0].islower():
#             for alp in variable:
#                 if alp.lower() not in small:
#                     return 'Error!'
#                 name = list(map(str, variable))
#                 idx = 0
#                 while idx < len(name):
#                     if name[idx].isupper():
#                         name[idx] = name[idx].lower()
#                         name.insert(idx, '_')
#                         idx += 1
#                     idx += 1
#                 return ''.join(name)
#         return 'Error!'
# print(change_type())


#1037 약수
# N = int(input())
# real = sorted(list(map(int, input().split())))
# number = real[-1] * 2
# while True:
#     for i in range(N-1):
#         if number%real[i] != 0:
#             number += real[-1]
#             break
#     else:
#         break
# print(number)



#1267 핸드폰 요금
# from math import ceil
# N = int(input())
# call_list = list(map(int, input().split()))
# price = {'Y':0, 'M':0}
# for call in call_list:
#     price['Y'] += ceil(call/30) * 10
#     price['M'] += ceil(call/60) * 15
# if price['Y'] == price['M']:
#     print('Y', 'M', price.get('Y'))
# elif price['Y'] < price['M']:
#     print('Y', price['Y'])
# else:
#     print('M', price['M'])


#2738 행렬 덧셈
# N, M = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(N)]
# def plus(a,b):
#     return a+b
# for i in range(N):
#     matrix[i] = list(map(plus, matrix[i], list(map(int, input().split()))))
#     print(*matrix[i])


# N, M = map(int, input().split())
# maxrix = [list(map(int, input().split())) for _ in range(N)]
# for i in range(N):
#     temp = list(map(int, input().split()))
#     for j in range(M):
#         maxrix[i][j] += temp[j]
#     print(*maxrix[i])