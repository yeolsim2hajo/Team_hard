#4358 생태학
# 왜 틀렸지....
# def calc_ratio():
#     from sys import stdin
#     new_input = stdin.readline
#     total = 0
#     species = {}
#     while True:
#         tree = new_input().rstrip()
#         if not tree:
#             keys = sorted(species)
#             for key in keys:
#                 print(key, round(species[key] / total * 100, 4))
#             return
#         if species.get(tree):
#             species[tree] += 1
#         else:
#             species[tree] = 1
#         total += 1
#
# calc_ratio()


#4097 수익
# from sys import stdin
# new_input = stdin.readline
# while True:
#     N = int(new_input())
#     if not N:
#         break
#     profit = int(new_input())
#     profits = [profit]
#     acc = [profit]
#     for _ in range(N-1):
#         profit = int(new_input())
#         profits.append(profit)
#         acc.append(profit)
#         acc[-1] += acc[-2]
#     print(max(*acc, *profits))


#15651 N과 M (3)
# N, M = map(int, input().split())
# path = []
# def dfs(arg=0):
#     if arg == M:
#         print(*path)
#         return
#     for i in range(1,N+1):
#         path.append(i)
#         dfs(arg+1)
#         path.pop()
# dfs()
