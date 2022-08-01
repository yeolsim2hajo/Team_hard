#1342
# 팩토리얼(라이브러리 쓰면 메모리 늘어나고 시간 약간 줄어듦)  + 재귀
# from collections import defaultdict
# from math import factorial
# S = input()
# N = len(S)
# check = defaultdict(int)
# keys = set()
# for alp in S:
#     check[alp] += 1
#     keys.add(alp)
# M = len(keys)
# if M == N:
#     total = factorial(N)
# else:
#     total = 0
#     def dfs(arg, new):
#         global total
#         if arg == N:
#             total += 1
#             return
#         for key in keys:
#             if check.get(key):
#                 if new == '' or new[-1] != key:
#                     check[key] -= 1
#                     dfs(arg+1, new+key)
#                     check[key] += 1
#     dfs(0,'')
#
# print(total)


# M 없애기
# from collections import defaultdict
# S = input()
# N = len(S)
# check = defaultdict(int)
# keys = set()
# for alp in S:
#     check[alp] += 1
#     keys.add(alp)
# if len(keys) == N:
#     total = 1
#     for i in range(2, N+1):
#         total *= i
# else:
#     total = 0
#     def dfs(arg, new):
#         global total
#         if arg == N:
#             total += 1
#             return
#         for key in keys:
#             if check.get(key):
#                 if new == '' or new[-1] != key:
#                     check[key] -= 1
#                     dfs(arg+1, new+key)
#                     check[key] += 1
#     dfs(0,'')
#
# print(total)


#defaultdict 안 쓰기 - 시간, 메모리 덜 나옴
# S = input()
# N = len(S)
# check = {}
# keys = set()
# for alp in S:
#     if check.get(alp):
#         check[alp] += 1
#     else:
#         check[alp] = 1
#         keys.add(alp)
# if len(keys) == N:
#     total = 1
#     for i in range(2, N+1):
#         total *= i
# else:
#     total = 0
#     def dfs(arg, new):
#         global total
#         if arg == N:
#             total += 1
#             return
#         for key in keys:
#             if check.get(key):
#                 if new == '' or new[-1] != key:
#                     check[key] -= 1
#                     dfs(arg+1, new+key)
#                     check[key] += 1
#     dfs(0,'')
#
# print(total)