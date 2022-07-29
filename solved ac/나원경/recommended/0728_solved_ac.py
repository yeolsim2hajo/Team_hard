#11561 징검다리
# import sys
# new_input = sys.stdin.readline
# T = int(new_input())
# def find_number():
#     start, end = 1, N
#     while start <= end:
#         number = (start+end)//2
#         total = number*(number+1)
#         if N == total//2:
#             return number
#         elif N < total//2:
#             end = number - 1
#         else:
#             start = number + 1
#     return end
#
# for _ in range(T):
#     N = int(new_input())
#     print(find_number())

# 시간 많이 걸림
# T = int(input())
# def find_number():
#     start, end = 1, N
#     while start <= end:
#         number = (start+end)//2
#         total = number*(number+1)
#         if N == total//2:
#             return number
#         elif N < total//2:
#             end = number - 1
#         else:
#             start = number + 1
#     return end
#
# for _ in range(T):
#     N = int(input())
#     print(find_number())

# //2까지
# import sys
# new_input = sys.stdin.readline
# T = int(new_input())
# def find_number():
#     start, end = 1, N
#     while start <= end:
#         number = (start+end)//2
#         total = number*(number+1)//2
#         if N == total:
#             return number
#         elif N < total:
#             end = number - 1
#         else:
#             start = number + 1
#     return end
#
# for _ in range(T):
#     N = int(new_input())
#     print(find_number())

# ceil - 시간 좀 더 걸림
# from math import ceil
# import sys
# new_input = sys.stdin.readline
# T = int(new_input())
# def find_number():
#     start, end = 1, N
#     while start <= end:
#         number = ceil((start+end)/2)
#         total = ceil(number*(number+1)/2)
#         if N == total:
#             return number
#         elif N < total:
#             end = number - 1
#         else:
#             start = number + 1
#     return end
#
# for _ in range(T):
#     N = int(new_input())
#     print(find_number())

# 시간 더 걸림
# import sys
# new_input = sys.stdin.readline
# T = int(new_input())
# def find_number():
#     start, end = 1, N
#     while start <= end:
#         number = int((start+end)/2)
#         total = int(number*(number+1)/2)
#         if N == total:
#             return number
#         elif N < total:
#             end = number - 1
#         else:
#             start = number + 1
#     return end
#
# for _ in range(T):
#     N = int(new_input())
#     print(find_number())

# 많은 순으로
import sys
new_input = sys.stdin.readline
T = int(new_input())
def find_number():
    start, end = 1, N
    while start <= end:
        number = (start+end)//2
        total = number*(number+1)//2
        if N < total:
            end = number - 1
        elif N > total:
            start = number + 1
        else:
            return number
    return end

for _ in range(T):
    N = int(new_input())
    print(find_number())