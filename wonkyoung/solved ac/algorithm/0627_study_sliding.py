#12847 꿀 아르바이트
# N, M = map(int, input().split())
# salary = list(map(int,input().split()))
# max_val = val = sum(salary[:M])
# for i in range(1,N-M+1):
#     val += salary[i+M-1] - salary[i-1]
#     if val > max_val:
#         max_val = val
# print(max_val)


#14602 소금과 후추 (Small)
# 하다 만 코드
# from collections import deque
# from statistics import median
# M, N, K, W = map(int, input().split())
# picture = [list(map(int, input().split())) for _ in range(M)]
# matrix = []
# answer = []
# def find_median(y,x=0,option=0):
#     global matrix, answer
#     if option:
#         for dy in range(M-W+1):
#             val = matrix[y+dy].popleft()
#             matrix[y+dy].append(picture[y+dy][x+W-1])
#             answer.append(picture[y+dy][x+W-1])
#             answer.remove(val)
#             print(matrix, answer)
#     else:
#         matrix = []
#         answer = []
#         for dy in range(W):
#             matrix.append(deque(picture[y+dy][x:x+W]))
#             answer.extend(picture[y+dy][x:x+W])
#     return median(answer)
#
# new_matrix = [[0] * (N-W+1) for _ in range(M-W+1)]
# for i in range(M-W+1):
#     for j in range(N-W+1):
#         if j == 0:
#             new_matrix[i][j] = find_median(i)
#         else:
#             new_matrix[i][j] = find_median(i,j,1)
#         print(new_matrix)
#
# for i in range(M-W+1):
#     print(*new_matrix[i])


# deque 이용
# from collections import deque
# M, N, K, W = map(int, input().split())
# picture = [list(map(int, input().split())) for _ in range(M)]
# check = deque()
# def find_median(y,x=0,option=0):
#     global check
#     from statistics import median
#     if option:
#         for dy in range(W):
#             check.remove(picture[y+dy][x-1])
#             check.append(picture[y+dy][x+W-1])
#     else:
#         check = deque()
#         for dy in range(W):
#             for dx in range(W):
#                 check.append(picture[y+dy][x+dx])
#     return median(check)
#
# new_matrix = [[0] * (N-W+1) for _ in range(M-W+1)]
# for i in range(M-W+1):
#     for j in range(N-W+1):
#         if j == 0:
#             new_matrix[i][j] = find_median(i)
#         else:
#             new_matrix[i][j] = find_median(i,j,1)
#
# for i in range(M-W+1):
#     print(*new_matrix[i])



# deque X - 약간 더 느림
# M, N, K, W = map(int, input().split())
# picture = [list(map(int, input().split())) for _ in range(M)]
# check = []
# def find_median(y,x=0,option=0):
#     global check
#     from statistics import median
#     if option:
#         for dy in range(W):
#             check.remove(picture[y+dy][x-1])
#             check.append(picture[y+dy][x+W-1])
#     else:
#         check = []
#         for dy in range(W):
#             for dx in range(W):
#                 check.append(picture[y+dy][x+dx])
#     return median(check)
#
# new_matrix = [[0] * (N-W+1) for _ in range(M-W+1)]
# for i in range(M-W+1):
#     for j in range(N-W+1):
#         if j == 0:
#             new_matrix[i][j] = find_median(i)
#         else:
#             new_matrix[i][j] = find_median(i,j,1)
#
# for i in range(M-W+1):
#     print(*new_matrix[i])



#24499 blobyum
# N, K = map(int,input().split())
# yum = list(map(int, input().split()))
# max_total = total = sum(yum[:K])
# for i in range(1,N):
#     end = i+K-1
#     if i+K-1 >= N:
#         end -= N
#     total += yum[end] - yum[i-1]
#     max_total = max(max_total, total)
# print(max_total)


#2559 수열
# N, K = map(int,input().split())
# temperature = list(map(int,input().split()))
# total = max_val = sum(temperature[:K])
# for i in range(1,N-K+1):
#     total += temperature[i+K-1] - temperature[i-1]
#     max_val = max(max_val, total)
# print(max_val)

# N, K = map(int,input().split())
# temperature = list(map(int,input().split()))
# total = max_val = sum(temperature[:K])
# for i in range(1,N-K+1):
#     total += temperature[i+K-1] - temperature[i-1]
#     if total > max_val:
#         max_val = total
# print(max_val)