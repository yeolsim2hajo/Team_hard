#230310
# N = int(input())
# nums = list(map(int, input().split()))
# max_num = nums[0]
# total = 0
# for num in nums:
#     if total >= 0:
#         total += num
#     else:
#         total = num
#     if total > max_num:
#         max_num = total
# print(max_num)
'''
5
-5 -4 -3 -2 -1
'''

#
def find_max():
    N = int(input())
    nums = list(map(int, input().split()))
    max_num = nums[0]
    total = 0
    for num in nums:
        if total >= 0:
            total += num
        else:
            total = num
        if total > max_num:
            max_num = total
    return max_num

print(find_max())

