#17124 두 개의 배열
# import sys
# T = int(input())
# new_input = sys.stdin.readline
# for _ in range(T):
#     N, M = map(int, new_input().split())
#     A = list(map(int, new_input().split()))
#     B = list(map(int, new_input().split()))
#     B.sort()
#     total = 0
#     for number in A:
#         if number <= B[0]:
#             total += B[0]
#         elif number >= B[-1]:
#             total += B[-1]
#         else:
#             def change_total():
#                 start, end = 0, M-1
#                 while start <= end:
#                     mid = (start + end) // 2
#                     if B[mid] == number:
#                         return B[mid]
#                     elif B[mid] > number:
#                         end = mid - 1
#                     else:
#                         start = mid + 1
#                 if number < B[end]:
#                     if B[end] - number > abs(number - B[end-1]):
#                         return B[end-1]
#                 elif number - B[end] > abs(number - B[end+1]):
#                     return B[end+1]
#                 return B[end]
#             total += change_total()
#     print(total)

# sys import X - 시간 더 걸림
# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     B.sort()
#     total = 0
#     for number in A:
#         if number <= B[0]:
#             total += B[0]
#         elif number >= B[-1]:
#             total += B[-1]
#         else:
#             def change_total():
#                 start, end = 0, M-1
#                 while start <= end:
#                     mid = (start + end) // 2
#                     if B[mid] == number:
#                         return B[mid]
#                     elif B[mid] > number:
#                         end = mid - 1
#                     else:
#                         start = mid + 1
#                 if number < B[end]:
#                     if B[end] - number > abs(number - B[end-1]):
#                         return B[end-1]
#                 elif number - B[end] > abs(number - B[end+1]):
#                     return B[end+1]
#                 return B[end]
#             total += change_total()
#     print(total)


# heap 사용 - 시간 더 걸림
# from heapq import heapify, heappop
# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     heapify(A)
#     B = list(map(int, input().split()))
#     B.sort()
#     total = 0
#     start, end = 0, M-1
#     for _ in range(N):
#         number = heappop(A)
#         if number <= B[start]:
#             total += B[start]
#         elif number >= B[end]:
#             total += B[end]
#         else:
#             def change_total():
#                 global start, end
#                 while start <= end:
#                     mid = (start + end) // 2
#                     if B[mid] == number:
#                         start = mid
#                         return B[mid]
#                     elif B[mid] > number:
#                         end = mid - 1
#                     else:
#                         start = mid + 1
#                 start = end
#                 if number > B[end] and number - B[end] > abs(number - B[end+1]):
#                     start += 1
#                 return B[start]
#             total += change_total()
#             end = M-1
#     print(total)


# 시간 초과
# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = set(map(int, input().split()))
#     total = 0
#     for number in A:
#         if number in B:
#             total += number
#         else:
#             def change_total():
#                 dif = 1
#                 while True:
#                     if (number - dif) in B:
#                         return (number - dif)
#                     elif (number + dif) in B:
#                         return (number + dif)
#                     dif += 1
#             total += change_total()
#     print(total)


# 정렬 안 하기 - 시간 초과
# import sys
# T = int(input())
# new_input = sys.stdin.readline
# for _ in range(T):
#     N, M = map(int, new_input().split())
#     A = list(map(int, new_input().split()))
#     B = list(map(int, new_input().split()))
#     total = 0
#     for number in A:
#         def change_total():
#             idx = 0
#             min_dif = answer = 1e9
#             while idx < M:
#                 dif = abs(B[idx] - number)
#                 if dif == 0:
#                     return number
#                 if dif < min_dif:
#                     min_dif = abs(dif)
#                     answer = B[idx]
#                 elif dif == min_dif and answer > number:
#                     answer = B[idx]
#                 idx += 1
#             return answer
#         total += change_total()
#     print(total)