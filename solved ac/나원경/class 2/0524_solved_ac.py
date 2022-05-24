#2108 통계학
# N = int(input())
# numbers = []
# max_val = -4000
# min_val = 4000
# total = 0
# check = {}
# for _ in range(N):
#     number = int(input())
#     if number > max_val:
#         max_val = number
#     if number < min_val:
#         min_val = number
#     if check.get(number):
#         check[number] += 1
#     else:
#         check[number] = 1
#     total += number
#     numbers.append(number)
# numbers.sort()
# conf = 1
# max_keys = []
# for key in check.keys():
#     if conf < check[key]:
#         max_keys = [key]
#         conf = check[key]
#     elif conf == check[key]:
#         max_keys.append(key)
# if len(max_keys) == 1:
#     max_keys = max_keys[0]
# else:
#     max_keys = sorted(max_keys)[1]
#
# print(int(total/N), numbers[N//2],max_keys,max_val-min_val, sep='\n')



# 카드2
# N = int(input())
# if N == 1:
#     print(1)
# else:
#     cards = list(range(2,N+1,2))
#     if N%2:
#         idx = 0
#     else:
#         cards = list(range(2,N+1,2))
#         idx = -1
#     while len(cards) > 1:
#         cards.pop(idx+1)
#         idx += 1
#         if idx == len(cards) - 1:
#             idx = -1
#         elif idx == len(cards):
#             idx = 0
#     print(cards[0])

#2231 분해합
N = input()
length = len(N)
N = int(N)
start = max(N - 9*length,1)
for num in range(start, N):
    if num + sum([int(n) for n in str(num)]) == N:
        print(num)
        break
else:
    print(0)


# number = sum(map(str))