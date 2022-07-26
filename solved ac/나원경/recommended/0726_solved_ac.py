#16507 전공책
# from collections import defaultdict
# word = input()
# N = int(input())
# books = []
# visited = [False] * N
# possible = False
# check = defaultdict(int)
# def find_min_sum(arg=0, total=0, plus=''):
#     global min_total, possible
#     if total > min_total:
#         return
#     if arg == i:
#         for alp in plus:
#             check[alp] += 1
#         for alp in word:
#             if check[alp]:
#                 check[alp] -= 1
#             else:
#                 check.clear()
#                 return
#         possible = True
#         min_total = total
#         check.clear()
#         return
#     for j in range(N):
#         if visited[j] is False:
#             visited[j] = True
#             find_min_sum(arg+1, total+books[j][0], plus+books[j][1])
#             visited[j] = False
#
# min_total = 0
# for _ in range(N):
#     price, book = input().split()
#     price = int(price)
#     books.append([price, book])
#     min_total += price
# # 사용할 전공책 숫자 (1 ~ N)
# for i in range(1,N+1):
#     find_min_sum()
# if possible:
#     print(min_total)
# else:
#     print(-1)
