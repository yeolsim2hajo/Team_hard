#230129
# possible_list = input()
# dices = sorted(map(int, input().split()))
# dice_check = [0] * 7
# cnt = 0
# possible_result = set(i+1 for i in range(12) if possible_list[i] == 'Y')
# # score = {
# #     7: lambda x, y: 3 * x + 2 * y,
# #     8: lambda x: (set(x))
# # }
# for dice in dices:
#     if dice_check[dice] == 0:
#         cnt += 1
#     dice_check[dice] += 1
#
# def find_max(cnt):
#     max_val = 0
#     match_func = ['']
#     for i in range(1, 7):
#         match_func.append(lambda multiple: i*multiple)
#     match_func.extend([
#         lambda num: num * 4,
#         lambda two, three: two*2 + three*3,
#         lambda num_list: 30 if set(num_list) == set(range(1, 6)) else 0,
#         lambda num_list: 30 if set(num_list) == set(range(2, 7)) else 0,
#         50,
#         sum
#     ])
#     #
#     #     9
#     #     10
#     #     11 : 50,
#     #     12 : lambda num_list: sum(num_list)
#     # ]
#     # )
#     # match_func.
#     if cnt == 1:
#         number = dices[0]
#         # Yacht, Choice, Ones ~ Sixes, Four of kind
#         if 11 in possible_result:
#             return 50
#         for i in (12, number, 7, 8):
#             if 12 in possible_result:
#                 value = max(number * 5, number * 3 + 6 * 2)
#                 if value > max_val:
#                     max_val = value
#             if number in possible_result:
#                 value = number * 5
#                 if value > max_val:
#                     max_val = value
#             if 7 in possible_result:
#                 value = number * 4
#                 if value > max_val:
#                     max_val = value
#             if 8 in possible_result:
#                 value = number * 3 + 6 * 2
#                 if value > max_val:
#                     max_val = value
#         return max_val
#
#     elif cnt == 2:
#         pass
#     else:
#         pass
#
# find_max(1)
# # # 한 숫자
# # max_total = 0
# # dice_num = over_four = 0
# # for i in possible_list:
# #     if i <= 6:
# #         total = (dice_check[i] + 2) * i
# #     elif
# #     if max_total < total:
# #         max_total = total

# 220130
score_list = input()
dice_list = sorted(map(int, input().split()))
over_two = 0
for i in range(2):
    before, after = dice_list[i:i+2]
    if before == after:
        over_two = before
dice_set = set(dice_list)
length = len(dice_set)
max_score = 0
for num in range(1, 6):
    if score_list[num-1] == 'Y':
        if num in dice_list:
            score = (6 - length) * num
        else:
            score = (5 - length) * num
        if score > max_score:
            max_score = score

if score_list[6] == 'Y' and over_two:
    score = over_two * 4

if score_list[7] == 'Y' and length == 2:
    score = dice_list[0] * 2 + dice_list[-1] * 3

if length == 3:
    for index, num in (8, 6), (9, 1):
        if score_list[index] == 'Y' and num not in dice_set:
            score = 30
            if max_score < score:
                max_score = score
if score_list[10] == 'Y' and length == 1:
    max_score = 50
if score_list[11] == 'Y':
    score = sum(dice_list) + 12
print(max_score)




