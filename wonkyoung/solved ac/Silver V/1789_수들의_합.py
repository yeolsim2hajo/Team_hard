#230123
# from math import isqrt
# S = int(input())
# limit = isqrt(2*S)
# total = limit * (limit+1) // 2
# for i in range(limit, 0, -1):
#     if total <= S:
#         print(i)
#         break
#     total -= i


# 함수
# def find_number(input_num):
#     from math import isqrt
#     limit = isqrt(2 * input_num)
#     total = limit * (limit + 1) // 2
#     for i in range(limit, 0, -1):
#         if total <= input_num:
#             return i
#         total -= i
#
# S = int(input())
# print(find_number(S))

# while
# def find_number(input_num):
#     from math import isqrt
#     limit = isqrt(2 * input_num)
#     total = limit * (limit + 1) // 2
#     num = limit
#     while True:
#         if total <= input_num:
#             return num
#         num -= 1
#         total -= num
#
# S = int(input())
# print(find_number(S))


# isqrt X - 시간 더 걸림
# def find_number(input_num):
#     total = 1
#     num = 1
#     while True:
#         if total > input_num:
#             return num - 1
#         if total == input_num:
#             return num
#         num += 1
#         total += num
#
# S = int(input())
# print(find_number(S))

# 이분탐색
# def find_number(input_num):
#     start, end = 1, input_num
#     while start <= end:
#         mid = (start + end) // 2
#         total = mid * (mid + 1) // 2
#         if total > input_num:
#             end = mid - 1
#         elif total < input_num:
#             start = mid + 1
#         else:
#             return mid
#     return end
#
# S = int(input())
# print(find_number(S))

# S로 대체
def find_number():
    start, end = 1, S
    while start <= end:
        mid = (start + end) // 2
        total = mid * (mid + 1) // 2
        if total > S:
            end = mid - 1
        elif total < S:
            start = mid + 1
        else:
            return mid
    return end

S = int(input())
print(find_number())