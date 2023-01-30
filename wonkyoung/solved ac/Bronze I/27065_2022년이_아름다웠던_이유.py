#230115
# import sys
#
# new_input = sys.stdin.readline
# T = int(new_input())
# numbers = [''] * 5001
# def is_special_number(n):
#     global numbers
#     good_bye, boj_2022 = 'Good Bye', 'BOJ 2022'
#
#     # over_num =
#     about_n = numbers[n]
#     if about_n == '':
#         for i in range(n//2):
#             pass
#     elif about_n == 'over':
#         pass
#     else:
#         return good_bye
#
#
# for _ in range(T):
#     n = int(new_input())
#     print(is_special_number(n))
# print()

#230118
import sys
new_input = sys.stdin.readline
T = int(new_input())
numbers = [''] * 5001
div_num_list = [set() for _ in range(5001)]


def is_special_number(n):
    from math import isqrt
    global numbers
    good_bye, boj_2022 = 'Good Bye', 'BOJ 2022'
    over, not_over = 'over', 'not_over'

    def is_not_over_number(m):
        isqrt_m = isqrt(m)
        for j in div_num_list[m]:
            if numbers[j] == '':
                isqrt_j = isqrt(j)

            elif numbers[j] == over:
                return good_bye


        if isqrt_m * isqrt_m == n:
            plus_n[n] -= isqrt_m
        if plus_n[m] < m:
            numbers[m] = over
            return good_bye

    about_n = numbers[n]
    isqrt_n = isqrt(n)
    plus_n = [0] * (n+1)
    if about_n == '':
        for i in range(1, isqrt_n+1):
            if n%i == 0:
                quot = n//i
                plus_n[n] += i + quot
                div_num_list[n].update([i, quot])
        if isqrt_n * isqrt_n == n:
            plus_n[n] -= isqrt_n
        if plus_n[n] < n:
            numbers[n] = over
            return is_not_over_number(n)
        else:
            numbers[n] = not_over
            return good_bye
    elif about_n == 'over':
        return is_not_over_number(n)
    else:
        return good_bye


for _ in range(T):
    n = int(new_input())
    print(is_special_number(n))