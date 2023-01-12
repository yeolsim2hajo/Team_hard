#221003
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# cnt = 0
# nonrecommend = [set() for _ in range(N+1)]
# for _ in range(M):
#     num1, num2 = sorted(map(int, new_input().split()))
#     nonrecommend[num1].add(num2)
# if N >= 3:
#     for i in range(1, N-1):
#         for j in range(i+1, N):
#             if j not in nonrecommend[i]:
#                 for k in range(j+1, N+1):
#                     if k not in nonrecommend[i] and k not in nonrecommend[j]:
#                         cnt += 1
# print(cnt)


# 함수로
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# nonrecommend = [set() for _ in range(N+1)]
# for _ in range(M):
#     num1, num2 = sorted(map(int, new_input().split()))
#     nonrecommend[num1].add(num2)
#
# def change_cnt():
#     cnt = 0
#     if N >= 3:
#         for i in range(1, N-1):
#             for j in range(i+1, N):
#                 if j not in nonrecommend[i]:
#                     for k in range(j+1, N+1):
#                         if k not in nonrecommend[i] and k not in nonrecommend[j]:
#                             cnt += 1
#     return cnt
#
# print(change_cnt())

# 함수로 2
# def change_cnt():
#     import sys
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     cnt = 0
#     nonrecommend = [set() for _ in range(N+1)]
#     for _ in range(M):
#         num1, num2 = sorted(map(int, new_input().split()))
#         nonrecommend[num1].add(num2)
#
#     if N >= 3:
#         for i in range(1, N-1):
#             for j in range(i+1, N):
#                 if j not in nonrecommend[i]:
#                     for k in range(j+1, N+1):
#                         if k not in nonrecommend[i] and k not in nonrecommend[j]:
#                             cnt += 1
#     return cnt
#
# print(change_cnt())


# 차집합 활용 - 조합이 되지 않음 - 수정 필요
# def change_cnt():
#     import sys
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     cnt = 0
#     nonrecommend = [set() for _ in range(N+1)]
#     for _ in range(M):
#         num1, num2 = sorted(map(int, new_input().split()))
#         nonrecommend[num1].add(num2)
#     if N >= 3:
#         for i in range(1, N-1):
#             print('i', i)
#             icecream = set(range(i+1, N)) - nonrecommend[i]
#             print('ice',icecream)
#             for j in icecream:
#                 recommend = icecream - nonrecommend[j] - {j}
#                 print('rec', recommend)
#                 cnt += len(recommend)
#                 print(cnt)
#     return cnt
#
# print(change_cnt())