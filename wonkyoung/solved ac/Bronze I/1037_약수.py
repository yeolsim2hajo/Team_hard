#230104
# 틀림
# cnt = int(input())
# numbers = sorted(map(int, input().split()))
# if cnt > 1:
#     answer = 1
#     for number in numbers:
#         if answer%number:
#             answer *= number
# else:
#     answer = (numbers[0])**2
# print(answer)

#230308
# N = int(input())
# div_num = list(map(int, input().split()))
# print(max(div_num) * min(div_num))


#
# N = int(input())
# max_num, min_num = 0, 1e6
# for num in map(int, input().split()):
#     if max_num < num:
#         max_num = num
#     if min_num > num:
#         min_num = num
# print(max_num * min_num)


#
def find_num():
    N = int(input())
    max_num, min_num = 0, 1e6
    for num in map(int, input().split()):
        if max_num < num:
            max_num = num
        if min_num > num:
            min_num = num
    return max_num * min_num
print(find_num())
