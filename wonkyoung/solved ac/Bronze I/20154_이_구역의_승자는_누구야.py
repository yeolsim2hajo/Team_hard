#230322
# cnt = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]
# alp_to_cnt = {chr(65+i):cnt[i] for i in range(26)}
# pre_arr = [alp_to_cnt[alp] for alp in input()]
# next_arr = []
# length = len(pre_arr)
# while length > 1:
#     for i in range(0, length-1, 2):
#         next_arr.append(pre_arr[i] + pre_arr[i+1])
#     if length%2:
#         next_arr.append(pre_arr[-1])
#     length = len(next_arr)
#     pre_arr = next_arr[:]
#     next_arr = []
# if pre_arr[0]%2:
#     print('I\'m a winner!')
# else:
#     print('You\'re the winner?')


#
# cnt = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]
# alp_to_cnt = {chr(65+i):cnt[i] for i in range(26)}
# pre_arr = [alp_to_cnt[alp] for alp in input()]
# next_arr = []
# length = len(pre_arr)
# while length > 1:
#     for i in range(0, length-1, 2):
#         next_arr.append(pre_arr[i] + pre_arr[i+1])
#
#     if length%2:
#         next_arr.append(pre_arr[-1])
#         length = length//2 + 1
#     else:
#         length = length//2
#     pre_arr = next_arr[:]
#     next_arr = []
#
# if pre_arr[0]%2:
#     print('I\'m a winner!')
# else:
#     print('You\'re the winner?')


#
# def find_winner():
#     cnt = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
#     alp_to_cnt = {chr(65 + i): cnt[i] for i in range(26)}
#     pre_arr = [alp_to_cnt[alp] for alp in input()]
#     next_arr = []
#     length = len(pre_arr)
#     while length > 1:
#         half = length//2
#         for i in range(half):
#             twice = 2*i
#             next_arr.append(pre_arr[twice] + pre_arr[twice + 1])
#
#         if length % 2:
#             next_arr.append(pre_arr[-1])
#             length = half + 1
#         else:
#             length = half
#         pre_arr = next_arr[:]
#         next_arr = []
#
#     return 'I\'m a winner!' if pre_arr[0] % 2 else 'You\'re the winner?'
# print(find_winner())


# 시간 초과
def find_winner():
    cnt = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
    alp_to_cnt = {chr(65 + i): cnt[i] for i in range(26)}
    num_arr = [alp_to_cnt[alp] for alp in input()]
    length = len(num_arr)
    while length > 1:
        half = length//2
        for i in range(half):
            num_arr[i] += num_arr[i+1]
            num_arr.pop(i+1)
        length = half + length%2

    return 'I\'m a winner!' if num_arr[0] % 2 else 'You\'re the winner?'
print(find_winner())
