# #230218
# def mix_solution():
#     N = int(input())
#     solution_list = list(map(int, input().split()))
#     if solution_list[0] >= 0:
#         return sum(solution_list[:2])
#     elif solution_list[-1] <= 0:
#         return sum(solution_list[-2:])
#
#     near_zero, flag = int(2e8), 1
#     left, right = 0, N-1
#     negative, positive = solution_list[left], solution_list[right]
#     while left < right:
#         total = negative + positive
#         if total > 0:
#             right -= 1
#             positive = solution_list[right]
#             if total < near_zero:
#                 near_zero, flag = total, 1
#         elif total < 0:
#             left += 1
#             negative = solution_list[left]
#             if -total < near_zero:
#                 near_zero, flag = -total, 0
#         else:
#             return 0
#     return near_zero if flag else -near_zero
#
#
# print(mix_solution())


#
def mix_solution():
    N = int(input())
    solution_list = list(map(int, input().split()))
    if solution_list[0] >= 0:
        return sum(solution_list[:2])
    elif solution_list[-1] <= 0:
        return sum(solution_list[-2:])

    left, right = 0, N - 1
    negative, positive = solution_list[left], solution_list[right]
    if positive >= -negative:
        near_zero, flag = positive*2, 1
    else:
        near_zero, flag = -negative*2, 0
    while left < right:
        total = negative + positive
        if total > 0:
            right -= 1
            positive = solution_list[right]
            new_flag = 1
        elif total < 0:
            left += 1
            negative = solution_list[left]
            total, new_flag = -total, 0
        else:
            return 0

        if total < near_zero:
            near_zero, flag = total, new_flag
    return near_zero if flag else -near_zero

print(mix_solution())