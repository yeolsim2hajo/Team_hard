#230216
# 부분 성공
# N = int(input())
# numbers = list(map(int, input().split()))
# signal = [''] * (N-1)
# for i in range(N-1):
#     if numbers[i] < numbers[i+1]:
#         signal[i] = '+'
#     elif numbers[i] > numbers[i+1]:
#         signal[i] = '-'
# max_length = 2
# for i in range(N-2):
#     for j in range(i, N-2):
#         if not signal[j] or not signal[j+1]:
#             break
#         elif signal[j] == signal[j+1]:
#             break
#         elif max_length < 3 + (j-i):
#             max_length = 3 + (j-i)
# print(max_length)


#
# N = int(input())
# numbers = list(map(int, input().split()))
# signal = [''] * (N-1)
# for i in range(N-1):
#     if numbers[i] < numbers[i+1]:
#         signal[i] = '+'
#     elif numbers[i] > numbers[i+1]:
#         signal[i] = '-'
# max_length = length = 2
# for i in range(N-2):
#     if not signal[i] or not signal[i + 1]:
#         length = 2
#         continue
#     elif signal[i] == signal[i+1]:
#         length = 2
#         continue
#     else:
#         length += 1
#         if length > max_length:
#             max_length = length
# print(max_length)


#
# N = int(input())
# numbers = list(map(int, input().split()))
# signal = [''] * (N-1)
# for i in range(N-1):
#     if numbers[i] < numbers[i+1]:
#         signal[i] = '+'
#     elif numbers[i] > numbers[i+1]:
#         signal[i] = '-'
# max_length = length = 2
# for i in range(N-2):
#     if not signal[i] or not signal[i + 1]:
#         length = 2
#     elif signal[i] == signal[i+1]:
#         length = 2
#     else:
#         length += 1
#         if length > max_length:
#             max_length = length
# print(max_length)


#
def cnt_length(N, numbers):
    signal = [''] * (N-1)
    for i in range(N-1):
        if numbers[i] < numbers[i+1]:
            signal[i] = '+'
        elif numbers[i] > numbers[i+1]:
            signal[i] = '-'

    max_length = length = 2
    for i in range(N-2):
        if not signal[i] or not signal[i + 1]:
            length = 2
        elif signal[i] == signal[i+1]:
            length = 2
        else:
            length += 1
            if length > max_length:
                max_length = length
    return max_length

N = int(input())
numbers = list(map(int, input().split()))
print(cnt_length(N, numbers))


